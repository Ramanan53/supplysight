-- =========================================================
-- SupplySight Database Schema (MySQL / ANSI SQL compatible)
-- =========================================================

CREATE DATABASE IF NOT EXISTS SupplySight;
USE SupplySight;

-- Drop existing tables for clean setup
DROP TABLE IF EXISTS Inventory;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Suppliers;
DROP TABLE IF EXISTS Warehouses;

-- 1. SUPPLIERS TABLE
CREATE TABLE Suppliers (
    Supplier_ID VARCHAR(20) PRIMARY KEY,
    Supplier_Name VARCHAR(100) NOT NULL,
    City VARCHAR(50) NOT NULL,
    Lead_Time_Days INT NOT NULL,
    Rating DECIMAL(3, 1) NOT NULL,
    On_Time_Delivery_Rate DECIMAL(5, 2) NOT NULL
);

-- 2. PRODUCTS TABLE
CREATE TABLE Products (
    Product_ID VARCHAR(20) PRIMARY KEY,
    Product_Name VARCHAR(100) NOT NULL,
    Category VARCHAR(50) NOT NULL,
    Unit_Cost DECIMAL(10, 2) NOT NULL,
    Unit_Price DECIMAL(10, 2) NOT NULL,
    Supplier_ID VARCHAR(20),
    FOREIGN KEY (Supplier_ID) REFERENCES Suppliers(Supplier_ID) ON DELETE SET NULL
);

-- 3. WAREHOUSES TABLE
CREATE TABLE Warehouses (
    Warehouse_ID VARCHAR(20) PRIMARY KEY,
    Warehouse_Name VARCHAR(100) NOT NULL,
    Location VARCHAR(50) NOT NULL,
    Capacity INT NOT NULL
);

-- 4. INVENTORY TABLE
CREATE TABLE Inventory (
    Inventory_ID VARCHAR(20) PRIMARY KEY,
    Product_ID VARCHAR(20) NOT NULL,
    Warehouse_ID VARCHAR(20) NOT NULL,
    Current_Stock INT NOT NULL,
    Reorder_Level INT NOT NULL,
    Monthly_Sales INT NOT NULL,
    Defect_Count INT DEFAULT 0,
    FOREIGN KEY (Product_ID) REFERENCES Products(Product_ID) ON DELETE CASCADE,
    FOREIGN KEY (Warehouse_ID) REFERENCES Warehouses(Warehouse_ID) ON DELETE CASCADE
);

-- Optimization Indexes for Analytics Performance
CREATE INDEX idx_products_category ON Products(Category);
CREATE INDEX idx_inventory_stock ON Inventory(Current_Stock, Reorder_Level);
