import pandas as pd
import numpy as np
import os

print("⚡ Starting SCM Transformation & Feature Engineering...")

base_dir = os.path.dirname(os.path.dirname(__file__))
cleaned_dir = os.path.join(base_dir, "Dataset", "cleaned")

# Load cleaned CSVs
products = pd.read_csv(os.path.join(cleaned_dir, "cleaned_products.csv"))
suppliers = pd.read_csv(os.path.join(cleaned_dir, "cleaned_suppliers.csv"))
inventory = pd.read_csv(os.path.join(cleaned_dir, "cleaned_inventory.csv"))
warehouses = pd.read_csv(os.path.join(cleaned_dir, "cleaned_warehouses.csv"))

# ---------------------------------------------------------
# 1. MERGE INVENTORY WITH PRODUCT DETAILS
# ---------------------------------------------------------
# Join Inventory with Products to get Unit_Cost, Unit_Price, Category, Supplier_ID
df = inventory.merge(products, on="Product_ID", how="left")

# ---------------------------------------------------------
# 2. CALCULATE INVENTORY VALUE & STOCK STATUS
# ---------------------------------------------------------
df["Inventory_Value"] = df["Current_Stock"] * df["Unit_Cost"]
df["Potential_Revenue"] = df["Current_Stock"] * df["Unit_Price"]
df["Profit_Margin_Per_Unit"] = df["Unit_Price"] - df["Unit_Cost"]

# Categorize Stock Status
def get_stock_status(row):
    if row["Current_Stock"] == 0:
        return "Out of Stock"
    elif row["Current_Stock"] <= row["Reorder_Level"]:
        return "Low Stock"
    elif row["Current_Stock"] > (row["Reorder_Level"] * 3):
        return "Overstocked"
    else:
        return "Optimal"

df["Stock_Status"] = df.apply(get_stock_status, axis=1)

# ---------------------------------------------------------
# 3. ABC INVENTORY ANALYSIS (PARETO 80/20 RULE)
# ---------------------------------------------------------
# Sort by total inventory value descending
df = df.sort_values(by="Inventory_Value", ascending=False).reset_index(drop=True)

# Calculate cumulative percentage of total inventory value
total_val = df["Inventory_Value"].sum()
df["Cumulative_Value"] = df["Inventory_Value"].cumsum()
df["Cumulative_Percentage"] = (df["Cumulative_Value"] / total_val) * 100

def get_abc_category(cum_pct):
    if cum_pct <= 70.0:
        return "Class A"  # High Value (Top 70%)
    elif cum_pct <= 90.0:
        return "Class B"  # Medium Value (Next 20%)
    else:
        return "Class C"  # Low Value (Bottom 10%)

df["ABC_Category"] = df["Cumulative_Percentage"].apply(get_abc_category)

# ---------------------------------------------------------
# 4. EXPORT FINAL MASTER DATASET FOR POWER BI & SQL
# ---------------------------------------------------------
final_master_path = os.path.join(cleaned_dir, "master_inventory_transformed.csv")
df.to_csv(final_master_path, index=False)

print("\n--- Transformation Summary ---")
print(f"Total Inventory Value: ${total_val:,.2f}")
print("\nStock Status Breakdown:")
print(df["Stock_Status"].value_counts())
print("\nABC Classification Breakdown:")
print(df["ABC_Category"].value_counts())
print(f"\n✅ Transformed dataset saved to: {final_master_path}")
