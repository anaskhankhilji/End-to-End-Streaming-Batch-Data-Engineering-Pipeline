import dlt
from dlt.sources.sql_database import sql_database

# Source: Module 1 ka Postgres database
source = sql_database(
    "postgresql://de_user:de_password@172.17.0.1:5432/de_project",
    table_names=["customers"]
)

# Destination: Amazon Redshift
pipeline = dlt.pipeline(
    pipeline_name="customers_redshift_pipeline",
    destination=dlt.destinations.redshift(
        credentials={
            "host": "default-workgroup.083141433583.us-east-1.redshift-serverless.amazonaws.com",
            "port": 5439,
            "database": "dev",
            "username": "de-project-namespace",
            "password": "MyProject123!"
        }
    ),
    dataset_name="raw_data"
)

# Run karo
load_info = pipeline.run(source)
print(load_info)
