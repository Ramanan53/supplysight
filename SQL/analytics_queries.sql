-- =========================================================
-- SupplySight Business Analytics Queries
-- =========================================================
USE SupplySight;

-- ---------------------------------------------------------
-- QUERY 1: Stockout Emergency & Replenishment Alert
-- Business Problem: Which items need immediate reorder to prevent sales loss?
-- ---------------------------------------------------------
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

-- ---------------------------------------------------------
-- QUERY 2: Supplier Reliability & On-Time Performance Ranking
-- Tech Concept: Window Function (DENSE_RANK)
-- Business Problem: Rank suppliers by delivery efficiency and rating within each city.
-- ---------------------------------------------------------
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

-- ---------------------------------------------------------
-- QUERY 3: Capital Lockup & Inventory Value by Category & Warehouse
-- Business Problem: Where is our money tied up in unsold inventory?
-- ---------------------------------------------------------
SELECT 
    w.Warehouse_Name,
    p.Category,
    COUNT(i.Inventory_ID) AS Total_SKUs,
    SUM(i.Current_Stock) AS Total_Stock_Units,
    SUM(i.Current_Stock * p.Unit_Cost) AS Total_Inventory_Value_USD,
    ROUND(AVG(i.Current_Stock * p.Unit_Cost), 2) AS Avg_Value_Per_SKU
FROM Inventory i
JOIN Products p ON i.Product_ID = p.Product_ID
JOIN Warehouses w ON i.Warehouse_ID = w.Warehouse_ID
GROUP BY w.Warehouse_Name, p.Category
ORDER BY Total_Inventory_Value_USD DESC;

-- ---------------------------------------------------------
-- QUERY 4: Stock Velocity & Overstock Identification
-- Tech Concept: Common Table Expression (CTE)
-- Business Problem: Identify items overstocked with > 3x reorder level vs monthly sales velocity.
-- ---------------------------------------------------------
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
    Product_ID,
    Product_Name,
    Category,
    Current_Stock,
    Reorder_Level,
    Stock_Value,
    Stock_Category
FROM StockAnalysis
WHERE Stock_Category = 'Overstocked'
ORDER BY Stock_Value DESC;
