# Azure Data Factory + Databricks ETL Pipeline

This project demonstrates an end-to-end data engineering pipeline built using
Azure Data Factory and Azure Databricks.

The pipeline ingests data from Azure SQL Database, processes and transforms data
using PySpark in Databricks, and stores curated data in Azure Data Lake using
Delta Lake format for analytics and reporting.

## Tech Stack
- Azure Data Factory
- Azure Databricks
- PySpark
- Delta Lake
- Azure SQL Database
- Azure Data Lake

## Key Features
- Parameterized ADF pipelines
- Incremental data loading
- PySpark-based data transformation
- Delta Lake optimized storage
- Analytics-ready curated layer

## Use Case
Sales transaction data is ingested, cleaned, enriched, and prepared for
Power BI and analytics workloads.
