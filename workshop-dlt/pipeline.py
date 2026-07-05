import dlt
from dlt.sources.sql_database import sql_database

# Source: Module 1 ka Postgres database
source = sql_database(
    "postgresql://de_user:de_password@172.17.0.1:5432/de_project",
    table_names=["customers"]
)

# Pipeline define karo
pipeline = dlt.pipeline(
    pipeline_name="customers_pipeline",
    destination="duckdb",
    dataset_name="raw_data"
)

# Run karo
load_info = pipeline.run(source)
print(load_info)
