# Azure Data Factory + Databricks ETL Pipeline

This repository demonstrates an end-to-end **Azure Data Engineering pipeline**
built using **Azure Data Factory and Azure Databricks**, following modern
enterprise data architecture principles.

## Business Problem
Organizations receive transactional sales data from relational systems that
must be processed, cleaned, and optimized for analytics and reporting.

## Solution Overview
The pipeline ingests data from Azure SQL Database using Azure Data Factory,
performs transformations using PySpark in Databricks, and stores curated data
in Delta Lake format on Azure Data Lake for downstream analytics (Power BI,
Synapse).

## Architecture
Azure SQL Database  
→ Azure Data Factory (ADF)  
→ Azure Data Lake (Raw Layer)  
→ Azure Databricks (Transformations)  
→ Delta Lake (Curated Layer)

## Tech Stack
- Azure Data Factory
- Azure Databricks
- PySpark
- Delta Lake
- Azure SQL Database
- Azure Data Lake Storage

## Key Features
- Parameterized ADF pipelines
- Incremental data loading using watermark column
- PySpark-based transformations
- Delta Lake partitioning for performance
- Analytics-ready curated data layer

## Use Case
Prepared data can be consumed by Power BI or Azure Synapse Analytics for
reporting and business insights.
