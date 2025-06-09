import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Load the combined dataset
file_path = "../data/combined_shipment_data.csv"
df = pd.read_csv(file_path)

# Select features and target
features = ['max_capacity', 'packages_ordered', 'fuel_surcharge']
target = 'logistics_cost'

X = df[features]
y = df[target]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    'Linear Regression': LinearRegression(),
    'Random Forest': RandomForestRegressor(random_state=42),
    'Gradient Boosting': GradientBoostingRegressor(random_state=42)
}

results = []

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    results.append((name, mae, r2))

# Print and save results
print("\n📊 Model Comparison:")
with open("../results/model_comparison.txt", "w") as f:
    for name, mae, r2 in results:
        line = f"{name:20} | MAE: {mae:.2f} | R2: {r2:.2f}"
        print(line)
        f.write(line + "\n")
