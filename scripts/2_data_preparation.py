import pandas as pd
import os

# Folder where supplier CSVs are stored
data_folder = "../data"

supplier_files = [
    "supplier_A_shipments.csv",
    "supplier_B_shipments.csv",
    "supplier_C_shipments.csv"
]

combined_data = pd.DataFrame()
for file in supplier_files:
    file_path = os.path.join(data_folder, file)
    df = pd.read_csv(file_path)
    combined_data = pd.concat([combined_data, df], ignore_index=True)

# Save combined dataset
combined_csv_path = os.path.join(data_folder, "combined_shipment_data.csv")
combined_data.to_csv(combined_csv_path, index=False)
print("✅ Combined dataset created at:", combined_csv_path)
