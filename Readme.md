# 📦 SupplySight: End-to-End Supply Chain Inventory Analytics & Intelligence System
> **Technical & Analytical Project Report**  
> **Domain**: Supply Chain Management (SCM), Logistics & Business Intelligence  
> **Stack**: Excel, Python (Pandas/NumPy), MySQL (ANSI SQL), Power BI (DAX)

---

## 1. 🎯 Executive Summary

**SupplySight** is an enterprise-grade, end-to-end Supply Chain Analytics solution engineered to optimize inventory holding costs, mitigate stockout risks, evaluate vendor reliability, and maximize working capital efficiency across multi-warehouse distribution networks.

By processing raw transactional data through a robust ETL pipeline in **Python**, structuring data into a **3NF MySQL Relational Database**, running analytical queries via **Advanced SQL**, and delivering real-time decision support via **Power BI**, SupplySight translates complex operational data into actionable strategic insights.

```
┌──────────────────┐      ┌──────────────────┐      ┌──────────────────┐      ┌──────────────────┐
│   Raw Datasets   │ ───> │ Python (Pandas)  │ ───> │ MySQL Database   │ ───> │ Power BI Engine  │
│ (Excel 4 Sheets) │      │ Cleaning & ETL   │      │ (3NF Relational) │      │  DAX Dashboards  │
└──────────────────┘      └──────────────────┘      └──────────────────┘      └──────────────────┘
```

### Key Performance Highlights & Executive Metrics
* **Total Working Capital Analyzed**: **$690,957.00** in total inventory value evaluated across distribution centers.
* **Low Stock Emergency Alerts**: **3 SKUs** flagged with stock levels below or equal to reorder threshold (`Current_Stock` $\le$ `Reorder_Level`), requiring immediate purchase order issuance.
* **Overstocked Inventory Risk**: **7 SKUs** identified with stock holding exceeding 3x the reorder requirement, locking up non-performing capital.
* **ABC Pareto Segregation**: Automated 80/20 inventory categorization into **Class A** (Top 70% value / 6 SKUs), **Class B** (Next 20% value / 5 SKUs), and **Class C** (Bottom 10% value / 8 SKUs).

---

## 2. 💡 Business Problem Formulation

Supply chain managers routinely face conflicting operational pressures: holding excess inventory ties up working capital and increases warehousing costs, while carrying insufficient inventory leads to stockouts, delayed fulfillment, customer churn, and revenue loss.

### Strategic Questions Solved by SupplySight
1. **Capital Allocation**: Which product categories and warehouses account for the largest share of tied-up inventory capital?
2. **Reorder & Risk Mitigation**: Which products require immediate vendor replenishment to avoid stockout downtime?
3. **Overstock Efficiency**: Which items are severely overstocked and consuming excessive warehouse capacity?
4. **Supplier Reliability**: How do suppliers rank in terms of lead-time adherence and on-time delivery rate within each region?
5. **Inventory Prioritization**: How should inventory management protocols be differentiated based on item value density (ABC Pareto Analysis)?

---

## 3. 🛠 Technology Stack & System Architecture

| Pipeline Stage | Technology | Applied Methodologies & Concepts |
| :--- | :--- | :--- |
| **Data Ingestion** | Microsoft Excel (`.xlsx`) | Multi-entity data modeling across Products, Suppliers, Warehouses, and Inventory |
| **Data Cleaning & Pipeline** | Python 3.10+, Pandas, NumPy | Null value imputation (median/mean), schema validation, string sanitization, deduplication |
| **Feature Engineering & SCM** | Python | **ABC Pareto Analysis**, Stock Status classification rules, Margin & Valuation metrics |
| **Relational Database** | MySQL / ANSI SQL | **3NF Normalization**, Foreign Keys (`ON DELETE CASCADE`), Indexing for query speed |
| **Advanced SQL Analytics** | MySQL | **Window Functions** (`DENSE_RANK OVER PARTITION BY`), **CTEs** (`WITH`), Group aggregations |
| **Business Intelligence** | Power BI Desktop, DAX | **Star Schema Data Model**, Dynamic DAX Calculated Measures (`SUMX`, `CALCULATE`, `DIVIDE`) |

---

## 4. 🔄 Data Engineering & Python ETL Pipeline

The ETL pipeline consists of two modular scripts located in the `Python/` directory: `clean_data.py` and `transform_data.py`.

```
inventory_data.xlsx ──> [clean_data.py] ──> Cleaned CSVs ──> [transform_data.py] ──> master_inventory_transformed.csv
```

### A. Data Hygiene & Sanitation (`clean_data.py`)
- **Missing Value Handling**:
  - Missing supplier ratings imputed using median rating ($\text{Rating}_{\text{imputed}} = \text{Median}(\text{Rating})$).
  - Missing lead times imputed using mean lead time ($\text{LeadTime}_{\text{imputed}} = \lfloor \text{Mean}(\text{LeadTime}) \rceil$).
- **Data Type Integrity**: Explicit cast of stock parameters (`Current_Stock`, `Reorder_Level`, `Lead_Time_Days`) to standard integers.
- **Deduplication**: Strict deduplication across all 4 entity datasets.

### B. Feature Engineering & Supply Chain Metrics (`transform_data.py`)

#### 1. Financial Valuation & Margin Calculation
$$\text{Inventory Value} = \text{Current Stock} \times \text{Unit Cost}$$
$$\text{Potential Revenue} = \text{Current Stock} \times \text{Unit Price}$$
$$\text{Profit Margin Per Unit} = \text{Unit Price} - \text{Unit Cost}$$

#### 2. Stock Status Categorization Matrix
$$\text{Stock Status} = \begin{cases} 
\text{Out of Stock}, & \text{if } \text{Current Stock} = 0 \\
\text{Low Stock}, & \text{if } \text{Current Stock} \le \text{Reorder Level} \\
\text{Overstocked}, & \text{if } \text{Current Stock} > (3 \times \text{Reorder Level}) \\
\text{Optimal}, & \text{otherwise}
\end{cases}$$

#### 3. ABC Pareto Inventory Classification Algorithm
Products are sorted in descending order of total inventory value to compute cumulative percentage share:
$$\text{Cumulative Percentage} = \frac{\sum_{i=1}^{k} \text{Inventory Value}_i}{\sum_{j=1}^{N} \text{Inventory Value}_j} \times 100$$
- **Class A (Tight Control)**: Items representing the top **70.0%** of cumulative inventory value.
- **Class B (Moderate Control)**: Items representing the next **20.0%** (70.0% – 90.0%) of value.
- **Class C (Simple Control)**: Items representing the bottom **10.0%** (90.0% – 100.0%) of value.

---

## 5. 🗄 Relational Database Schema & Data Model

The relational schema strictly enforces **Third Normal Form (3NF)** to eliminate redundancy and maintain referential integrity.

```
       ┌────────────────────────┐                  ┌────────────────────────┐
       │       Suppliers        │                  │       Warehouses       │
       ├────────────────────────┤                  ├────────────────────────┤
       │ PK  Supplier_ID        │                  │ PK  Warehouse_ID       │
       │     Supplier_Name      │                  │     Warehouse_Name     │
       │     City               │                  │     Location           │
       │     Lead_Time_Days     │                  │     Capacity           │
       │     Rating             │                  └───────────┬────────────┘
       │     On_Time_Delivery   │                              │
       └───────────┬────────────┘                              │
                   │ (1:N)                                     │ (1:N)
                   ▼                                           │
       ┌────────────────────────┐                              │
       │        Products        │                              │
       ├────────────────────────┤                              │
       │ PK  Product_ID         │                              │
       │     Product_Name       │                              │
       │     Category           │                              │
       │     Unit_Cost          │                              │
       │     Unit_Price         │                              │
       │ FK  Supplier_ID        │                              │
       └───────────┬────────────┘                              │
                   │ (1:N)                                     │
                   └──────────────────┐   ┌────────────────────┘
                                      ▼   ▼
                          ┌────────────────────────┐
                          │       Inventory        │
                          ├────────────────────────┤
                          │ PK  Inventory_ID       │
                          │ FK  Product_ID         │
                          │ FK  Warehouse_ID       │
                          │     Current_Stock      │
                          │     Reorder_Level      │
                          │     Monthly_Sales      │
                          │     Defect_Count       │
                          └────────────────────────┘
```

### Table Definitions & Foreign Key Constraints
1. **Suppliers**: Primary Key `Supplier_ID`.
2. **Products**: Primary Key `Product_ID`, Foreign Key `Supplier_ID` $\rightarrow$ `Suppliers(Supplier_ID)` with `ON DELETE SET NULL`.
3. **Warehouses**: Primary Key `Warehouse_ID`.
4. **Inventory**: Primary Key `Inventory_ID`, Foreign Keys `Product_ID` $\rightarrow$ `Products(Product_ID)` and `Warehouse_ID` $\rightarrow$ `Warehouses(Warehouse_ID)` with `ON DELETE CASCADE`.

### Performance Indexing
```sql
CREATE INDEX idx_products_category ON Products(Category);
CREATE INDEX idx_inventory_stock ON Inventory(Current_Stock, Reorder_Level);
```

---

## 6. 🔍 Advanced SQL Analytical Engine

Below are key business intelligence queries executed against the relational database (found in `SQL/analytics_queries.sql`).

### Query 1: Emergency Replenishment & Stockout Alert
Identifies items requiring immediate PO issue based on stock vs. reorder thresholds.
```sql
SELECT 
    i.Inventory_ID,
    p.Product_Name,
    p.Category,
    w.Warehouse_Name,
    i.Current_Stock,
    i.Reorder_Level,
    s.Supplier_Name,
    s.Lead_Time_Days
FROM Inventory i
JOIN Products p ON i.Product_ID = p.Product_ID
JOIN Warehouses w ON i.Warehouse_ID = w.Warehouse_ID
JOIN Suppliers s ON p.Supplier_ID = s.Supplier_ID
WHERE i.Current_Stock <= i.Reorder_Level
ORDER BY i.Current_Stock ASC;
```

### Query 2: Regional Supplier Reliability Ranking (Window Functions)
Ranks vendors partitioned by city using `DENSE_RANK()` based on on-time delivery rate and overall rating.
```sql
SELECT 
    Supplier_ID,
    Supplier_Name,
    City,
    Rating,
    On_Time_Delivery_Rate,
    Lead_Time_Days,
    DENSE_RANK() OVER (PARTITION BY City ORDER BY On_Time_Delivery_Rate DESC, Rating DESC) AS Rank_In_City
FROM Suppliers
ORDER BY City, Rank_In_City;
```

### Query 3: Overstocked Capital Lockup Analysis (Common Table Expressions)
Uses a CTE to isolate items holding excess inventory ($>3\times \text{Reorder Level}$) and quantifies tied-up capital.
```sql
WITH StockAnalysis AS (
    SELECT 
        p.Product_ID,
        p.Product_Name,
        p.Category,
        i.Current_Stock,
        i.Reorder_Level,
        i.Monthly_Sales,
        (i.Current_Stock * p.Unit_Cost) AS Stock_Value,
        CASE 
            WHEN i.Current_Stock > (i.Reorder_Level * 3) THEN 'Overstocked'
            WHEN i.Current_Stock <= i.Reorder_Level THEN 'Understocked'
            ELSE 'Balanced'
        END AS Stock_Category
    FROM Inventory i
    JOIN Products p ON i.Product_ID = p.Product_ID
)
SELECT 
    Product_ID, Product_Name, Category, Current_Stock, Reorder_Level, Stock_Value, Stock_Category
FROM StockAnalysis
WHERE Stock_Category = 'Overstocked'
ORDER BY Stock_Value DESC;
```

---

## 7. 📈 Power BI Business Intelligence & DAX Engine

The Power BI dashboard operates on a Star Schema data model, utilizing custom DAX measures for dynamic slice-and-dice analytics.

### Formulated DAX Measures Matrix

```dax
-- 1. Executive Valuation Metrics
Total Inventory Value = 
SUMX(
    master_inventory_transformed,
    master_inventory_transformed[Current_Stock] * master_inventory_transformed[Unit_Cost]
)

Total Potential Revenue = 
SUMX(
    master_inventory_transformed,
    master_inventory_transformed[Current_Stock] * master_inventory_transformed[Unit_Price]
)

Overall Profit Margin % = 
DIVIDE(
    [Total Potential Revenue] - [Total Inventory Value],
    [Total Potential Revenue],
    0
) * 100

-- 2. Inventory Risk & Alert Measures
Stockout Risk Items = 
CALCULATE(
    COUNTROWS(master_inventory_transformed),
    master_inventory_transformed[Stock_Status] = "Low Stock"
)

Overstocked Items = 
CALCULATE(
    COUNTROWS(master_inventory_transformed),
    master_inventory_transformed[Stock_Status] = "Overstocked"
)

Inventory Turnover Ratio = 
DIVIDE(
    SUM(master_inventory_transformed[Monthly_Sales]),
    AVERAGE(master_inventory_transformed[Current_Stock]),
    0
)

-- 3. Supplier Performance Measures
Avg Supplier Lead Time = AVERAGE(cleaned_suppliers[Lead_Time_Days])

Avg On Time Delivery Rate = AVERAGE(cleaned_suppliers[On_Time_Delivery_Rate])
```

---

## 8. 📊 Key Business Insights & Strategic Action Plan

1. **Working Capital Realignment**:
   - **$690.9K** total inventory value is unevenly distributed; **Class A** SKUs represent 70% of financial exposure across only 6 high-value items.
   - **Recommendation**: Implement cycle counting and daily reorder monitoring for Class A items, while shifting Class C items to automated bulk replenishment.
2. **Overstock Capital Liquidating**:
   - 7 SKUs exceed $3\times$ reorder levels, resulting in unnecessary storage cost and holding risk.
   - **Recommendation**: Run promotional clearance or reallocate excess inventory across low-stock warehouses to free up working capital.
3. **Supplier SLA Optimization**:
   - Suppliers with low on-time delivery rates ($<85\%$) are primary drivers of stockout risks for critical SKUs.
   - **Recommendation**: Re-negotiate SLAs with low-ranked vendors based on the SQL `Rank_In_City` benchmarking model.

---

## 9. 📁 Project Structure & File Map

```
SupplySight/
│
├── Dataset/
│   ├── inventory_data.xlsx                  # Raw multi-sheet dataset (Products, Suppliers, Warehouses, Inventory)
│   ├── generate_dataset.py                  # Dataset generator script
│   └── cleaned/                             # Output directory for pipeline artifacts
│       ├── cleaned_products.csv             # Sanitized Products table
│       ├── cleaned_suppliers.csv            # Imputed & clean Suppliers table
│       ├── cleaned_warehouses.csv           # Validated Warehouses table
│       ├── cleaned_inventory.csv            # Cleaned raw Inventory table
│       └── master_inventory_transformed.csv # Master dataset engineered with ABC & Stock Status
│
├── Python/
│   ├── clean_data.py                        # ETL Script 1: Imputation, type casting, deduplication
│   └── transform_data.py                    # ETL Script 2: SCM feature engineering & ABC classification
│
├── SQL/
│   ├── schema.sql                           # 3NF DDL schema with Foreign Keys & Indexes
│   └── analytics_queries.sql                # Analytical SQL queries (CTEs, Window Functions)
│
├── PowerBI/
│   ├── SS.pbix                              # Power BI Dashboard file
│   └── DAX_Measures.md                      # Comprehensive DAX measures dictionary
│
├── Screenshots/                             # Dashboard visualizations & execution captures
├── .gitignore                               # Version control exclusions
├── requirements.txt                         # Python runtime dependencies
└── README.md                                # Master Technical Project Report
```

---

## 10. ⚡ Execution & Deployment Guide

### Step 1: Environment Setup
Clone the repository and install required Python packages:
```bash
git clone https://github.com/Ramanan53/supplysight.git
cd supplysight
pip install -r requirements.txt
```

### Step 2: Run Python ETL Data Pipeline
Execute data cleaning and feature engineering transformations:
```bash
python Python/clean_data.py
python Python/transform_data.py
```
*Outputs cleaned CSVs and `master_inventory_transformed.csv` in `Dataset/cleaned/`.*

### Step 3: Initialize MySQL Database
Execute schema setup and load data into MySQL:
```bash
mysql -u root -p < SQL/schema.sql
```
Run analytical queries:
```bash
mysql -u root -p SupplySight < SQL/analytics_queries.sql
```

### Step 4: Launch Power BI Report
1. Open `PowerBI/SS.pbix` in **Power BI Desktop**.
2. Update data source paths to point to `Dataset/cleaned/master_inventory_transformed.csv` and `cleaned_suppliers.csv` if required.
3. Refresh dataset to view dynamic visual dashboards.

---

## 📌 Resume Project Highlight

**Supply Chain Inventory Analytics & BI Dashboard | Python (Pandas), MySQL, Power BI (DAX), Excel**
- Architected an end-to-end Supply Chain Analytics solution analyzing **$690K+** in working capital across multi-warehouse hubs.
- Built automated Python ETL pipelines to impute missing vendor data, engineer SCM metrics, and perform **ABC Pareto 80/20 Inventory Classification**.
- Designed a **3NF MySQL Relational Database** schema with foreign key constraints and indexes; wrote queries using **CTEs** and **Window Functions** (`DENSE_RANK`) to evaluate vendor SLAs and capital lockup.
- Developed interactive Power BI dashboards utilizing **DAX measures** (`SUMX`, `CALCULATE`, `DIVIDE`) to deliver stockout emergency alerts and warehouse utilization insights.

---

## 🔮 Future Enhancements
- [ ] **Predictive Inventory Forecasting**: Integrate ARIMA/Prophet models in Python for demand forecasting.
- [ ] **Safety Stock & EOQ Calculator**: Implement Economic Order Quantity (EOQ) optimization algorithms.
- [ ] **Automated CI/CD ETL**: Orchestrate daily pipeline execution via Airflow or GitHub Actions.

---

## 📜 License
This project is open-source and licensed under the [MIT License](LICENSE).