# 📦 SupplySight – Supply Chain Inventory Analytics Dashboard

A Supply Chain Analytics project built to understand how companies manage inventory, suppliers, and warehouses using data. The project uses Excel as the data source, MySQL for data storage, Python for data processing, and Power BI for creating an interactive dashboard.

The main objective is to learn how data can help businesses make better supply chain decisions while improving SQL, Python, Excel, and Power BI skills.

---

## 🎯 Project Objective

The goal of this project is to analyze inventory data and answer common business questions such as:

- Which products need to be reordered?
- Which supplier delivers products on time?
- Which warehouse stores the highest inventory?
- Which products contribute the most inventory value?
- Which product categories perform the best?
- How can inventory be monitored efficiently?

This project focuses more on business analytics than web development.

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Excel | Sample inventory dataset |
| MySQL | Store and query inventory data |
| SQL | Business analysis queries |
| Python (Pandas) | Data cleaning and preprocessing |
| Power BI | Dashboard and visualization |

Python Libraries

- pandas
- numpy
- openpyxl

---

## 📁 Project Structure

```
SupplySight/

│
├── Dataset/
│   ├── inventory.xlsx
│   ├── suppliers.xlsx
│   └── warehouses.xlsx
│
├── SQL/
│   ├── schema.sql
│   ├── sample_data.sql
│   └── analytics_queries.sql
│
├── Python/
│   ├── clean_data.py
│   ├── transform_data.py
│   └── export_csv.py
│
├── PowerBI/
│   └── SupplySight.pbix
│
├── Screenshots/
│
├── README.md
│
└── requirements.txt
```

---

## 🗄 Database Tables

### Products

Stores product details.

Columns

- Product_ID
- Product_Name
- Category
- Unit_Cost
- Supplier_ID

---

### Suppliers

Stores supplier information.

Columns

- Supplier_ID
- Supplier_Name
- City
- Lead_Time_Days
- Rating

---

### Inventory

Stores stock details.

Columns

- Inventory_ID
- Product_ID
- Warehouse
- Current_Stock
- Reorder_Level
- Monthly_Sales

---

## 📊 Dashboard KPIs

The dashboard includes the following metrics:

- Total Products
- Total Inventory Value
- Low Stock Products
- Average Supplier Lead Time
- Top Selling Products
- Monthly Sales
- Warehouse-wise Inventory
- Supplier Performance

---

## 📈 Dashboard Visualizations

- KPI Cards
- Bar Chart
- Line Chart
- Pie Chart
- Matrix/Table
- Slicers

---

## 🧮 SQL Analysis

Some of the SQL queries used in this project include:

- Find products below reorder level
- Calculate total inventory value
- Supplier performance analysis
- Average supplier lead time
- Monthly sales summary
- Warehouse-wise stock report
- Category-wise inventory
- Top selling products

---

## 🐍 Python Tasks

Python is used to:

- Read Excel files
- Clean missing values
- Format dates
- Calculate inventory value
- Export cleaned data for Power BI

---

## 📊 Power BI Dashboard

The dashboard is built using the cleaned dataset and includes:

- Interactive filters
- KPI cards
- Inventory analysis
- Supplier analysis
- Warehouse analysis
- Product category analysis

The dashboard helps understand inventory trends and supplier performance in a simple and visual way.

---

## 💡 Business Questions Solved

This project answers questions like:

- Which products need immediate replenishment?
- Which suppliers have the shortest delivery time?
- Which warehouse stores the highest stock?
- Which category has the highest inventory value?
- Which suppliers perform the best?
- Which products are overstocked?
- Which products are running out of stock?

---

## 📚 Concepts Learned

### Supply Chain

- Inventory Management
- Warehouse Management
- Supplier Management
- Procurement
- Lead Time
- Reorder Point

### Data Analytics

- SQL Queries
- Data Cleaning
- Dashboard Design
- KPI Reporting
- Business Insights

---

## 🚀 Future Improvements

Some features that can be added later:

- Demand Forecasting
- ABC Inventory Analysis
- EOQ Calculator
- Safety Stock Calculation
- Inventory Turnover Ratio
- Automated Report Generation
- Power BI Service Deployment

---

## 📷 Screenshots

Screenshots of the Power BI dashboard will be added after completing the project.

---

## 🏆 Skills Demonstrated

- SQL
- MySQL
- Excel
- Python
- Power BI
- Data Cleaning
- Data Visualization
- Dashboard Development
- Business Analytics
- Supply Chain Analytics

---

## 📌 Resume Description

Developed a Supply Chain Inventory Analytics Dashboard using Excel, MySQL, SQL, Python, and Power BI. Performed data cleaning, inventory analysis, supplier performance evaluation, and created interactive dashboards to generate business insights for inventory planning and decision-making.

---

## 📖 What I Learned

Through this project, I gained practical experience in working with supply chain data. I learned how to clean and analyze datasets using Python, write SQL queries to answer business questions, and build interactive Power BI dashboards that help visualize inventory and supplier performance. This project also improved my understanding of basic supply chain concepts and business analytics.