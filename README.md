# **Dublin Transportation Data Warehouse**

This repository contains the implementation of a data warehouse for Dublin's public transportation data, including Luas passenger counts, Dublin Bus passenger counts, weather data, Dublin Bikes data, and cycle counts. The project demonstrates how to design, ingest, clean, and store data from multiple sources into Snowflake.

## **Project Objective**

The goal of this project is to evaluate the ability to design, implement, and optimize a data infrastructure for public transportation in Dublin, Ireland. The data warehouse was designed to:

1. Ingest and clean data from multiple sources.
2. Store the cleaned data in a scalable structure.
3. Enable future data ingestion and pipeline automation.

## **Contents**

- `sql/`: Contains SQL scripts to create tables and ingest data.
- `scripts/`: Python scripts for fetching and processing data.
- `data/`: Sample processed data files.
- `docs/`: Documentation of the data pipeline design.

---

## **Prerequisites**

### **Tools and Libraries**

- Snowflake: A trial account or equivalent data warehouse technology.
- Python 3.9+

### **Dependencies:**

- pandas
- requests
- openpyxl

Install the Python dependencies using:
```bash
pip install pandas requests openpyxl
```

**Setup Instructions**

**1. Create the Data Warehouse:**
   - Set up a Snowflake account (or equivalent data warehouse).
   - Open the worksheet section and run the SQL script located in `sql/create_tables.sql` to:
      - Create the database, schemas and tables for storing the cleaned data
      - Example query from create_tables.sql:
      
      ```sql
      CREATE DATABASE dublin_transport_db;
      CREATE SCHEMA luas;
      CREATE TABLE luas.passenger_counts (
      year INT NOT NULL,
      month STRING NOT NULL,
      line STRING NOT NULL,
      passengers INT NOT NULL
      );
      ```
**2. Fetch and Process Data**
   - Run the Python scripts to fetch and process data from various sources
   - Fetch Dublin Bikes Data:
      - This script fetches data for the last three months from the Dublin Bikes API.
    
        ```bash
        python scripts/fetch_dublin_bikes_data.py
        ```
   - Process Cycle Counts Data
      - This script processes cycle counts data from an Excel file

        ```bash
        python scripts/process_cycle_counts.py
        ```

**3. Load Data into Snowflake**
   - Open the Snowflake Web UI.
   - Navigate to the table where you want to upload the data.
   - Use the "Load Data" option to upload the corresponding CSV file (e.g., processed_cycle_counts.csv, dublin_bikes_last_3_months.csv).
   - Follow the steps in the UI to map the columns and load the data.

**4. Review Documentation**

Refer to docs/data_pipeline_design.md for the pipeline design and how it scales for future data sources.

**Folder structure**

```
.
├── README.md
├── sql/
│   ├── create_tables.sql
│   └── queries_used.sql
├── scripts/
│   ├── fetch_dublin_bikes_data.py
│   ├── process_cycle_counts.py
├── data/
│   ├── processed_cycle_counts.csv
│   ├── dublin_bikes_last_3_months.csv
├── docs/
│   └── data_pipeline_design.md
└── LICENSE
```

**Key Decisions**

1. Data Normalization:
   - Standardized column names for consistency across tables.
   - Converted blank cells to `NULL` while preserving zeros.
2. Date Handling:
   - Standardized all date formats to `YYYY-MM-DD` for consistency
   - Extracted `full_date` from `year` and `month` columns where possible
   - Kept `NULL` for yearly total rows in `luas.passenger_counts` and `dublin_bus.passenger_counts`
   - Retained both `TIMESTAMP` and `DATE` columns in `dublin_bikes.station_data` to preserve flexibility

---

## **Future Enhancements**

To further improve scalability and automation, the following enhancements can be implemented:

- **Automated Data Ingestion**
  - Set up Snowflake External Stages for streamlined ingestion.
  - Replace manual CSV uploads with an automated pipeline.
- **Incremental Data Loading**
  - Implement incremental data updates instead of full dataset replacements.
- **Query Performance Optimization**
  - Apply indexing and partitioning for faster query execution.
- **Enhanced Error Handling**
  - Improve exception handling in Python scripts to ensure reliability.

---

## **License**

This project is licensed under the MIT License. See the LICENSE file for more details.

