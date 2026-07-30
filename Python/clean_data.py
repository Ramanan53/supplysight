import pandas as pd
import numpy as np
import os

print("🧹 Starting Data Cleaning Process...")

# Define paths
base_dir = os.path.dirname(os.path.dirname(__file__))
raw_data_path = os.path.join(base_dir, "Dataset", "inventory_data.xlsx")

# 1. Read all sheets from raw Excel file
excel_file = pd.ExcelFile(raw_data_path)
products_df = pd.read_excel(excel_file, sheet_name="Products")
suppliers_df = pd.read_excel(excel_file, sheet_name="Suppliers")
warehouses_df = pd.read_excel(excel_file, sheet_name="Warehouses")
inventory_df = pd.read_excel(excel_file, sheet_name="Inventory")

# ---------------------------------------------------------
# CLEANING SUPPLIERS DATA
# ---------------------------------------------------------
print("\n--- Cleaning Suppliers Table ---")
print(f"Missing values before cleaning:\n{suppliers_df.isnull().sum()}")

# Fill missing Rating with median rating
median_rating = suppliers_df["Rating"].median()
suppliers_df["Rating"] = suppliers_df["Rating"].fillna(median_rating)

# Fill missing Lead_Time_Days with mean lead time (rounded)
mean_lead_time = round(suppliers_df["Lead_Time_Days"].mean())
suppliers_df["Lead_Time_Days"] = suppliers_df["Lead_Time_Days"].fillna(mean_lead_time)

print(f"✅ Missing values after cleaning:\n{suppliers_df.isnull().sum()}")

# ---------------------------------------------------------
# DATA TYPE INTEGRITY & DUP CHECKS
# ---------------------------------------------------------
# Ensure numerical types are clean
suppliers_df["Lead_Time_Days"] = suppliers_df["Lead_Time_Days"].astype(int)
inventory_df["Current_Stock"] = inventory_df["Current_Stock"].astype(int)
inventory_df["Reorder_Level"] = inventory_df["Reorder_Level"].astype(int)

# Remove any inadvertent duplicate rows
products_df.drop_duplicates(inplace=True)
suppliers_df.drop_duplicates(inplace=True)
warehouses_df.drop_duplicates(inplace=True)
inventory_df.drop_duplicates(inplace=True)

# ---------------------------------------------------------
# SAVE CLEANED INTERMEDIATE DATA
# ---------------------------------------------------------
cleaned_dir = os.path.join(base_dir, "Dataset", "cleaned")
os.makedirs(cleaned_dir, exist_ok=True)

products_df.to_csv(os.path.join(cleaned_dir, "cleaned_products.csv"), index=False)
suppliers_df.to_csv(os.path.join(cleaned_dir, "cleaned_suppliers.csv"), index=False)
warehouses_df.to_csv(os.path.join(cleaned_dir, "cleaned_warehouses.csv"), index=False)
inventory_df.to_csv(os.path.join(cleaned_dir, "cleaned_inventory.csv"), index=False)

print(f"\n✅ Cleaned datasets saved to: {cleaned_dir}")
