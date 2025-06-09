import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load shipment data from multiple CSV files
df_de = pd.read_csv('../data/supplier_A_shipments.csv')  # Germany
df_us = pd.read_csv('../data/supplier_B_shipments.csv')  # USA
df_cn = pd.read_csv('../data/supplier_C_shipments.csv')  # China

df_de['supplier'] = 'Germany'
df_us['supplier'] = 'USA'
df_cn['supplier'] = 'China'

df = pd.concat([df_de, df_us, df_cn], ignore_index=True)
df['date'] = pd.to_datetime(df['date'])

print(df.info())
print(df.describe())
print(df.head())

# Packages sent per supplier
plt.figure(figsize=(10,6))
sns.boxplot(data=df, x='supplier', y='packages_sent')
plt.title("Packages Sent per Shipment by Supplier")
plt.savefig('../results/figures/packages_sent_boxplot.png')
plt.show()

# Fuel surcharge distribution
plt.figure(figsize=(10,6))
sns.histplot(data=df, x='fuel_surcharge', hue='supplier', bins=20, kde=True, element='step')
plt.title("Fuel Surcharge Distribution by Supplier")
plt.savefig('../results/figures/fuel_surcharge_hist.png')
plt.show()

# Logistics cost over time
plt.figure(figsize=(14,7))
sns.lineplot(data=df, x='date', y='logistics_cost', hue='supplier')
plt.title("Logistics Cost Over Time by Supplier")
plt.savefig('../results/figures/logistics_cost_over_time.png')
plt.show()

# Penalty and expedite cost
print("Penalty Cost Stats:")
print(df['penalty_cost'].describe())
print("\nExpedite Cost Stats:")
print(df['expedite_cost'].describe())

plt.figure(figsize=(12,5))
plt.subplot(1, 2, 1)
sns.boxplot(data=df, x='supplier', y='penalty_cost')
plt.title('Penalty Cost by Supplier')

plt.subplot(1, 2, 2)
sns.boxplot(data=df, x='supplier', y='expedite_cost')
plt.title('Expedite Cost by Supplier')
plt.tight_layout()
plt.savefig('../results/figures/penalty_expedite_boxplot.png')
plt.show()

plt.figure(figsize=(14,6))
sns.lineplot(data=df, x='date', y='penalty_cost', hue='supplier', ci=None)
plt.title('Penalty Cost Over Time by Supplier')
plt.savefig('../results/figures/penalty_cost_over_time.png')
plt.show()

plt.figure(figsize=(14,6))
sns.lineplot(data=df, x='date', y='expedite_cost', hue='supplier', ci=None)
plt.title('Expedite Cost Over Time by Supplier')
plt.savefig('../results/figures/expedite_cost_over_time.png')
plt.show()
