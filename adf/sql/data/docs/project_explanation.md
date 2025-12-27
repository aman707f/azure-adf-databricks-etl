This project simulates a real-world enterprise data engineering workflow.

Azure Data Factory is used for orchestration and ingestion, while Databricks
handles scalable data transformations using PySpark. Data is stored in Delta
Lake format to support efficient analytics and reporting.

The architecture follows a layered approach: Raw, Processed, and Curated data.
