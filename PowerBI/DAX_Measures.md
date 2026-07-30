# 📊 SupplySight - Power BI DAX Measures Reference

This document lists key DAX (Data Analysis Expressions) calculated measures used in the SupplySight Power BI Dashboard.

---

## 1. Executive Key Performance Indicators (KPIs)

### Total Inventory Value ($)

```dax
Total Inventory Value =
SUMX(
    master_inventory_transformed,
    master_inventory_transformed[Current_Stock] * master_inventory_transformed[Unit_Cost]
)


### Total Potential Revenue ($)

dax
Total Potential Revenue =
SUMX(
    master_inventory_transformed,
    master_inventory_transformed[Current_Stock] * master_inventory_transformed[Unit_Price]
)


### Overall Profit Margin (%)


dax
Overall Profit Margin % =
DIVIDE(
    [Total Potential Revenue] - [Total Inventory Value],
    [Total Potential Revenue],
    0
) * 100


## 2. Inventory Risk & Alert Measures

### Stockout Risk Count (Low Stock Alerts)

dax
Stockout Risk Items =
CALCULATE(
    COUNTROWS(master_inventory_transformed),
    master_inventory_transformed[Stock_Status] = "Low Stock"
)


### Overstocked SKU Count

dax
Overstocked Items =
CALCULATE(
    COUNTROWS(master_inventory_transformed),
    master_inventory_transformed[Stock_Status] = "Overstocked"
)

### Inventory Turnover Ratio

dax
Inventory Turnover Ratio =
DIVIDE(
    SUM(master_inventory_transformed[Monthly_Sales]),
    AVERAGE(master_inventory_transformed[Current_Stock]),
    0
)


## 3. Supplier Performance DAX Measures

### Average Lead Time (Days)

dax
Avg Supplier Lead Time =
AVERAGE(cleaned_suppliers[Lead_Time_Days])

### On-Time Delivery Rate (%)

dax
Avg On Time Delivery Rate =
AVERAGE(cleaned_suppliers[On_Time_Delivery_Rate])

```
