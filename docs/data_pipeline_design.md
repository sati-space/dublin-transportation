# **Dublin Transportation Data Pipeline Design**

## **Overview**
This document describes the data pipeline for ingesting, transforming, and storing public transportation data in Dublin. The pipeline extracts data from various sources, cleans and normalizes it, and loads it into Snowflake.

## **Data Sources**
1. **Luas Passenger Counts** - CSV file uploaded manually
2. **Dublin Bus Passenger Counts** - CSV file uploaded manually
3. **Weather Data** - CSV file with daily records from Merrion Square Station
4. **Dublin Bikes** - API data fetched for the last 3 months
5. **Cycle Counts** - Excel file converted to CSV

## **Processing Steps**
1. **Data Extraction**
   - APIs (Dublin Bikes) → Python scripts fetch & save to CSV
   - Static files (Luas, Bus, Weather) → Uploaded manually

2. **Data Transformation**
   - Standardized date formats (`YYYY-MM-DD`)
   - Converted blank values to `NULL`
   - Renamed columns for consistency
   - Stored both `TIMESTAMP` & `DATE` for flexibility

3. **Data Loading**
   - Snowflake UI was used to load CSV files into tables.
   - Queries from `transform_data.sql` were run to format data.

## **Storage Strategy**
- Data is stored in a **star schema** format.
- Tables are divided by **schemas** for clarity (`luas`, `dublin_bus`, etc.).
- Date fields ensure proper **time-based analysis**.

## **Future Enhancements**
- Automate ingestion using **external Snowflake stages**.
- Implement **incremental data loads** instead of full replacements.
- Add **error handling** to Python scripts for robust execution.