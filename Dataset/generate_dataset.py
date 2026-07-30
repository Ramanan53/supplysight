import pandas as pd
import numpy as np
import os

# Ensure reproducible random data
np.random.seed(42)

print("📦 Generating Supply Chain Dataset...")

# ---------------------------------------------------------
# 1. SUPPLIERS DATA
# ---------------------------------------------------------
num_suppliers = 15
supplier_ids = [f"SUP-{100 + i}" for i in range(num_suppliers)]
supplier_names = [
    "Apex Logistics", "Global Freight Co", "Nexus Supply Chain", 
    "Vanguard Goods", "Horizon Traded", "Prime Distribution",
    "Atlas Components", "Zenith Materials", "Beacon Imports",
    "Pinnacle Source", "Quantum Supply", "Velocity Cargo",
    "Titan Cargo", "Echo Sourcing", "Omni Trade"
]
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Dallas", "Seattle"]

suppliers_df = pd.DataFrame({
    "Supplier_ID": supplier_ids,
    "Supplier_Name": supplier_names,
    "City": [np.random.choice(cities) for _ in range(num_suppliers)],
    "Lead_Time_Days": np.random.randint(3, 21, size=num_suppliers),  # Days to deliver stock
    "Rating": np.round(np.random.uniform(3.0, 5.0, size=num_suppliers), 1),
    "On_Time_Delivery_Rate": np.round(np.random.uniform(75.0, 99.0, size=num_suppliers), 1)
})

# Add 1-2 intentional nulls/dirty data for learning python data cleaning!
suppliers_df.loc[3, "Rating"] = np.nan
suppliers_df.loc[7, "Lead_Time_Days"] = np.nan

# ---------------------------------------------------------
# 2. PRODUCTS DATA
# ---------------------------------------------------------
categories = {
    "Electronics": ["Wireless Mouse", "Mechanical Keyboard", "27-inch Monitor", "USB-C Hub", "Noise Cancelling Headphones"],
    "Office Supplies": ["Ergonomic Chair", "Standing Desk", "Notebook Pack", "Desk Lamp", "Document Shredder"],
    "Warehouse Tools": ["Barcode Scanner", "Label Printer", "Packaging Tape Dispenser", "Hand Truck", "Pallet Jack"]
}

product_rows = []
prod_id_counter = 501

for category, prod_list in categories.items():
    for prod_name in prod_list:
        cost = np.random.randint(15, 300)
        margin = np.random.uniform(1.2, 1.6)
        price = round(cost * margin, 2)
        supplier_id = np.random.choice(supplier_ids)
        
        product_rows.append({
            "Product_ID": f"PROD-{prod_id_counter}",
            "Product_Name": prod_name,
            "Category": category,
            "Unit_Cost": cost,
            "Unit_Price": price,
            "Supplier_ID": supplier_id
        })
        prod_id_counter += 1

products_df = pd.DataFrame(product_rows)

# ---------------------------------------------------------
# 3. WAREHOUSES & INVENTORY DATA
# ---------------------------------------------------------
warehouses = [
    {"Warehouse_ID": "WH-EAST", "Warehouse_Name": "East Coast Distribution Center", "Location": "New Jersey", "Capacity": 50000},
    {"Warehouse_ID": "WH-WEST", "Warehouse_Name": "West Coast Logistics Hub", "Location": "California", "Capacity": 75000},
    {"Warehouse_ID": "WH-CENTRAL", "Warehouse_Name": "Central Storage Facility", "Location": "Texas", "Capacity": 60000}
]
warehouses_df = pd.DataFrame(warehouses)

inventory_rows = []
inv_id_counter = 1001

for _, prod in products_df.iterrows():
    # Assign each product to 1 or 2 warehouses
    selected_whs = np.random.choice([w["Warehouse_ID"] for w in warehouses], size=np.random.choice([1, 2]), replace=False)
    
    for wh_id in selected_whs:
        current_stock = np.random.randint(5, 500)
        reorder_level = np.random.randint(50, 150)
        monthly_sales = np.random.randint(20, 400)
        
        inventory_rows.append({
            "Inventory_ID": f"INV-{inv_id_counter}",
            "Product_ID": prod["Product_ID"],
            "Warehouse_ID": wh_id,
            "Current_Stock": current_stock,
            "Reorder_Level": reorder_level,
            "Monthly_Sales": monthly_sales,
            "Defect_Count": np.random.randint(0, 15)
        })
        inv_id_counter += 1

inventory_df = pd.DataFrame(inventory_rows)

# ---------------------------------------------------------
# 4. EXPORT TO EXCEL
# ---------------------------------------------------------
output_file = os.path.join(os.path.dirname(__file__), "inventory_data.xlsx")

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    products_df.to_excel(writer, sheet_name="Products", index=False)
    suppliers_df.to_excel(writer, sheet_name="Suppliers", index=False)
    warehouses_df.to_excel(writer, sheet_name="Warehouses", index=False)
    inventory_df.to_excel(writer, sheet_name="Inventory", index=False)

print(f"✅ Dataset generated successfully at: {output_file}")
