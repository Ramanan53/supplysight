# 📦 SupplySight – Supply Chain Inventory Analytics & BI Dashboard

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![SQL Engine](https://img.shields.io/badge/SQL-ANSI%2FMySQL-orange.svg)](https://www.mysql.com/)
[![Power BI](https://img.shields.io/badge/Power_BI-DAX-yellow.svg)](https://powerbi.microsoft.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A Supply Chain Analytics project built to understand how companies manage inventory, suppliers, and warehouses using data. The project uses Excel as the data source, MySQL for data storage, Python for data processing, and Power BI for creating an interactive dashboard.

---

## 🎯 Purpose & Project Objective

The purpose of this project is to understand how data analytics is used in supply chain management. By working with inventory, supplier, and warehouse data, the goal is to learn how businesses track stock levels, evaluate supplier performance, and make data-driven decisions.

This project also helps strengthen practical skills in **SQL, Python, Excel, and Power BI** while building an end-to-end analytics solution that reflects a real-world business scenario.

### Key Business Questions Solved:
- Which products need immediate replenishment?
- Which suppliers have the shortest delivery time and highest reliability?
- Which warehouse stores the highest stock value?
- Which product categories contribute the most inventory value?
- Which products are overstocked or at risk of stockout?

---

## 📊 Executive Business Impact & Key Metrics

Processed and analyzed using synthetic data modeled after real retail & warehouse operations:
- 💰 **Total Inventory Capital Analyzed**: **$690,957.00**
- ⚠️ **Low Stock Emergency Alerts**: **3 SKUs** flagged for immediate vendor reorder ($Current\_Stock \le Reorder\_Level$)
- 📦 **Overstocked SKUs**: **7 SKUs** identified with excessive stock holding (> 3x reorder level) draining working capital
- 🏷️ **ABC Pareto Classification**: Sorted inventory into **Class A** (Top 70% value / 6 SKUs), **Class B** (Next 20% value / 5 SKUs), and **Class C** (Bottom 10% value / 8 SKUs)

---

## 🛠 Tech Stack & System Architecture

```
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│   Raw Datasets  │  ───> │ Python (Pandas) │  ───> │ SQL Relational  │  ───> │    Power BI     │
│ (Excel 4 Sheets)│       │ Clean & Transform│       │  Database (3NF) │       │   Dashboard     │
└─────────────────┘       └─────────────────┘       └─────────────────┘       └─────────────────┘
```

| Layer | Technology | Key Applied Concept |
| :--- | :--- | :--- |
| **Data Ingestion** | Excel (`.xlsx`) | Multi-entity data modeling (Products, Suppliers, Warehouses, Inventory) |
| **ETL & Data Cleaning** | Python, Pandas, NumPy | Null value imputation (median/mean), String sanitation, Type integrity |
| **SCM Feature Eng.** | Python | **ABC Classification**, Stock Status categorization, Inventory Value computation |
| **Relational Database** | MySQL / ANSI SQL | 3NF Schema DDL, Foreign Keys (`ON DELETE CASCADE`), Indexing |
| **SQL Analytics** | SQL | **Window Functions** (`DENSE_RANK() OVER`), **CTEs** (`WITH`), Group aggregations |
| **BI & Visualization** | Power BI, DAX | Star Schema Data Model, Dynamic DAX Measures, Multi-page Dashboard |

---

## 📁 Project Structure

```
SupplySight/
│
├── Dataset/
│   ├── inventory_data.xlsx                 # Raw multi-sheet Excel dataset
│   ├── generate_dataset.py                 # Synthetic data generation script
│   └── cleaned/
│       ├── cleaned_products.csv
│       ├── cleaned_suppliers.csv
│       ├── cleaned_warehouses.csv
│       └── master_inventory_transformed.csv# Fully engineered dataset ready for Power BI
│
├── Python/
│   ├── clean_data.py                       # Data cleaning script (nulls, types, dups)
│   └── transform_data.py                   # SCM metrics & ABC analysis calculation
│
├── SQL/
│   ├── schema.sql                          # 3NF Database DDL with constraints & indexes
│   └── analytics_queries.sql               # Complex business queries (CTEs, Window functions)
│
├── PowerBI/
│   └── DAX_Measures.md                     # Documentation of dynamic DAX measures
│
├── Screenshots/                            # Dashboard screenshots
├── .gitignore
├── requirements.txt                        # Python dependencies
└── README.md
```

---

## 🗄 Database Table Specifications

### 1. Products
- `Product_ID` (PK)
- `Product_Name`
- `Category`
- `Unit_Cost`
- `Unit_Price`
- `Supplier_ID` (FK)

### 2. Suppliers
- `Supplier_ID` (PK)
- `Supplier_Name`
- `City`
- `Lead_Time_Days`
- `Rating`
- `On_Time_Delivery_Rate`

### 3. Warehouses
- `Warehouse_ID` (PK)
- `Warehouse_Name`
- `Location`
- `Capacity`

### 4. Inventory
- `Inventory_ID` (PK)
- `Product_ID` (FK)
- `Warehouse_ID` (FK)
- `Current_Stock`
- `Reorder_Level`
- `Monthly_Sales`
- `Defect_Count`

---

## 🧮 Core Supply Chain Analytics Formulas

1. **Inventory Value ($)**:
   $$\text{Inventory Value} = \text{Current Stock} \times \text{Unit Cost}$$

2. **Reorder Point (ROP)**:
   $$\text{ROP} = (\text{Average Daily Sales} \times \text{Supplier Lead Time Days}) + \text{Safety Stock}$$

3. **ABC Pareto Classification**:
   - **Class A**: Top 70% of total inventory value (High priority, tight daily control)
   - **Class B**: Next 20% of inventory value (Moderate control)
   - **Class C**: Bottom 10% of inventory value (Bulk / low-holding cost items)

---

## 🗄 Sample SQL Analytics Queries

### 1. Supplier Delivery Ranking by City (Window Functions)
```sql
SELECT 
    Supplier_ID, Supplier_Name, City, Rating, On_Time_Delivery_Rate,
    DENSE_RANK() OVER (PARTITION BY City ORDER BY On_Time_Delivery_Rate DESC, Rating DESC) AS Rank_In_City
FROM Suppliers;
```

### 2. Overstocked Inventory Identification (CTEs)
```sql
WITH StockAnalysis AS (
    SELECT p.Product_Name, i.Current_Stock, i.Reorder_Level, (i.Current_Stock * p.Unit_Cost) AS Stock_Value,
        CASE WHEN i.Current_Stock > (i.Reorder_Level * 3) THEN 'Overstocked' ELSE 'Optimal' END AS Stock_Category
    FROM Inventory i JOIN Products p ON i.Product_ID = p.Product_ID
)
SELECT * FROM StockAnalysis WHERE Stock_Category = 'Overstocked' ORDER BY Stock_Value DESC;
```

---

## 📚 Concepts Learned & Applied

### Supply Chain Domain
- Inventory Management & Stockout Risk Mitigation
- Warehouse Utilization & Capital Lockup
- Supplier Performance & Lead Time Tracking
- ABC Inventory Classification (Pareto Principle)

### Technical Analytics
- Data Cleaning & Imputation (Python/Pandas)
- 3NF Relational Database Modeling & Indexing (SQL)
- Complex Aggregations, CTEs & Window Functions (SQL)
- Star Schema Modeling & DAX Measures (Power BI)

---

## 📌 Resume Description

**Supply Chain Analytics & BI Dashboard | Excel, Python (Pandas), MySQL, Power BI**
- Developed an end-to-end Supply Chain Analytics solution analyzing **$690K+** in inventory capital across 3 distribution hubs.
- Built Python ETL scripts to clean dirty vendor data and compute **ABC Pareto Inventory Classifications** & **Reorder Points (ROP)**.
- Designed a **3NF MySQL database** and wrote analytical queries leveraging **CTEs** and **Window Functions** (`DENSE_RANK`) to evaluate supplier performance.
- Modeled interactive Power BI dashboards utilizing **DAX measures** (`SUMX`, `CALCULATE`, `DIVIDE`) to track stockout risks and capital lockup.

---

## 🚀 Future Improvements

- Demand Forecasting using Time-Series Models (ARIMA/Prophet).
- Economic Order Quantity (EOQ) & Safety Stock Calculator.
- Power BI Service Automated Refresh Deployment.

---

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).