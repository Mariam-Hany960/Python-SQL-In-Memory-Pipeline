# SQL Data Extraction & In-Memory Pipeline

## 📊 Project Overview
An automated, serverless data engineering pipeline designed to ingest commercial transaction logs from spreadsheets and process them using an in-memory database structure.

## 🚀 Key Features
- **Dynamic File Ingestion:** Uses Python (`Tkinter`) for an automated and flexible file selection workspace.
- **Data Engineering Engine:** Utilizes `Pandas` for robust data parsing and structured dataframe transformation.
- **Serverless SQL Database:** Mounts an in-memory `SQLite3` database (`:memory:`) to execute relational logic with zero infrastructure latency.
- **Advanced Query Analysis:** Runs comprehensive SQL evaluations, including Multi-dimensional Aggregations (`GROUP BY`, `SUM`, `AVG`), Pattern Matching (`LIKE`), and Hierarchical Ranking (`ORDER BY DESC`).

## 📁 Repository Structure
- `main.py`: The core Python data pipeline script.
- `Data_Analytics_Official_Final_Report.pdf`: The official technical project documentation and query results.
- `sales_dataset.xlsx`: The raw commercial transactional data spreadsheet used for ingestion.

## 🛠️ Technologies Used
- Python (Tkinter, Pandas)
- SQLite3
- Relational SQL
