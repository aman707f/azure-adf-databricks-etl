## Azure Data Factory Pipeline Overview

1. Source: Azure SQL Database
2. Sink: Azure Data Lake (Raw Layer)
3. Trigger: Scheduled (Daily)
4. Features:
   - Parameterized datasets
   - Incremental load using watermark column
   - Retry and failure handling

Pipeline Flow:
Azure SQL → ADF Copy Activity → Azure Data Lake → Databricks Notebook
