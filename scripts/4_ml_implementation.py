import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import minimize

# Load Data
file_path = "../data/combined_shipment_data.csv"
if not os.path.exists(file_path):
    raise FileNotFoundError("CSV file not found. Please check the file path.")

df = pd.read_csv(file_path)

# Group Weekly Data
weekly_data = df.groupby(['supplier', 'year', 'week']).agg({
    'logistics_cost': 'sum',
    'fuel_surcharge': 'mean',
    'packages_ordered': 'sum',
    'max_capacity': 'mean'
}).reset_index()

# One-hot Encode Supplier
encoder = OneHotEncoder(sparse=False)
supplier_encoded = encoder.fit_transform(weekly_data[['supplier']])
supplier_df = pd.DataFrame(supplier_encoded, columns=encoder.get_feature_names_out(['supplier']))

# Combine Features
X = pd.concat([
    weekly_data[['year', 'week', 'fuel_surcharge', 'packages_ordered']].reset_index(drop=True),
    supplier_df.reset_index(drop=True)
], axis=1)
y = weekly_data['logistics_cost']

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate Model
y_pred = model.predict(X_test)
print("\n📊 Overall Model Performance:")
print(f"MAE: {mean_absolute_error(y_test, y_pred):.2f}")
print(f"R² Score: {r2_score(y_test, y_pred):.2f}")

# --- GLOBAL OPTIMIZATION WITH PER-SUPPLIER TOTAL DEMAND CONSTRAINT ---

print("\n🔄 Globally optimizing shipments for lowest predicted cost (per-supplier total demand preserved)...")

bounds = [(0, mc) for mc in weekly_data['max_capacity']]

# Prepare features for all rows
supplier_ohe = encoder.transform(weekly_data[['supplier']])
base_features = weekly_data[['year', 'week', 'fuel_surcharge']].values

feature_names = ['year', 'week', 'fuel_surcharge', 'packages_ordered'] + list(encoder.get_feature_names_out(['supplier']))

def total_cost(packages):
    X_df = pd.DataFrame(
        np.hstack([
            base_features,
            packages.reshape(-1, 1),
            supplier_ohe
        ]),
        columns=feature_names
    )
    return model.predict(X_df).sum()

constraints = []
for supplier in weekly_data['supplier'].unique():
    idx = weekly_data.index[weekly_data['supplier'] == supplier].to_numpy()
    total_sup = weekly_data.loc[idx, 'packages_ordered'].sum()
    constraints.append({
        'type': 'eq',
        'fun': lambda x, idx=idx, total_sup=total_sup: np.sum(x[idx]) - total_sup
    })

result = minimize(
    total_cost,
    x0=weekly_data['packages_ordered'].values,
    bounds=bounds,
    constraints=constraints,
    method='SLSQP',
    options={'disp': True, 'maxiter': 1000}
)

weekly_data['optimized_packages_ordered'] = result.x

# Per Supplier: Original vs Optimized
results = []
for supplier in weekly_data['supplier'].unique():
    supplier_orig = weekly_data[weekly_data['supplier'] == supplier].copy()
    supplier_opt = supplier_orig.copy()
    supplier_opt['packages_ordered'] = supplier_opt['optimized_packages_ordered']

    supplier_encoded = encoder.transform(supplier_orig[['supplier']])
    supplier_ohe = pd.DataFrame(supplier_encoded, columns=encoder.get_feature_names_out(['supplier']))

    X_orig = pd.concat([
        supplier_orig[['year', 'week', 'fuel_surcharge', 'packages_ordered']].reset_index(drop=True),
        supplier_ohe.reset_index(drop=True)
    ], axis=1)

    X_opt = pd.concat([
        supplier_opt[['year', 'week', 'fuel_surcharge', 'packages_ordered']].reset_index(drop=True),
        supplier_ohe.reset_index(drop=True)
    ], axis=1)

    pred_orig = model.predict(X_orig)
    pred_opt = model.predict(X_opt)

    avg_orig = np.mean(pred_orig)
    avg_opt = np.mean(pred_opt)
    savings = avg_orig - avg_opt

    results.append({
        'Supplier': supplier,
        'Original_Cost': avg_orig,
        'Optimized_Cost': avg_opt,
        'Savings': savings
    })

results_df = pd.DataFrame(results).sort_values(by='Savings', ascending=False)
print("\n📊 Average Predicted Cost Comparison by Supplier:\n")
print(results_df.to_string(index=False))

# Plotting: Cost Comparison
plt.figure(figsize=(10, 6))
bar_width = 0.35
x = np.arange(len(results_df['Supplier']))

plt.bar(x - bar_width/2, results_df['Original_Cost'], bar_width, label='Original')
plt.bar(x + bar_width/2, results_df['Optimized_Cost'], bar_width, label='Optimized')

plt.xlabel('Supplier')
plt.ylabel('Predicted Average Cost')
plt.title('Predicted Logistics Cost per Supplier: Original vs Optimized')
plt.xticks(x, results_df['Supplier'])
plt.legend()
plt.tight_layout()
plt.grid(axis='y')
plt.savefig('../results/figures/cost_comparison.png')
plt.show()

# Plotting: Distribution of shipments per supplier per week
plot_df = weekly_data.copy()
plot_df_long = pd.melt(
    plot_df,
    id_vars=['supplier', 'year', 'week'],
    value_vars=['packages_ordered', 'optimized_packages_ordered'],
    var_name='Type',
    value_name='Shipments'
)
plot_df_long['Type'] = plot_df_long['Type'].map({
    'packages_ordered': 'Original',
    'optimized_packages_ordered': 'Optimized'
})

plot_df_long = plot_df_long.sort_values(['supplier', 'year', 'week', 'Type'])

g = sns.FacetGrid(
    plot_df_long,
    col='supplier',
    hue='Type',
    sharey=False,
    height=4,
    aspect=2,
    margin_titles=True
)
g.map(
    sns.lineplot, 'week', 'Shipments', marker='o'
).add_legend()

g.set_axis_labels("Week", "Number of Shipments")
g.set_titles("Supplier: {col_name}")
g.fig.subplots_adjust(top=0.85)
g.fig.suptitle("Weekly Shipment Distribution: Original vs Optimized", fontsize=16)
plt.savefig('../results/figures/weekly_shipment_distribution.png')
plt.show()

# Verify per-supplier constraints
print("\nPer-supplier shipment verification:")
for supplier in weekly_data['supplier'].unique():
    orig = weekly_data[weekly_data['supplier'] == supplier]['packages_ordered'].sum()
    opt = weekly_data[weekly_data['supplier'] == supplier]['optimized_packages_ordered'].sum()
    print(f"Supplier {supplier}: original={orig:.0f}, optimized={opt:.0f}")
