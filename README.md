### 🚀 Nexus Data Platform

End-to-end streaming and batch data engineering pipeline — from raw source data to business-ready dashboards, built entirely on AWS.
Nexus connects multiple independent systems — streaming, batch, orchestration, warehousing, and analytics — into one unified data platform.

### 🏗️ Architecture

<img width="1774" height="887" alt="ChatGPT Image Jul 4, 2026, 10_28_11 PM" src="https://github.com/user-attachments/assets/b82b7d8a-2d46-4d84-8c7a-0c037e5f670c" />

### 📖 Overview

Nexus Data Platform is a hands-on, production-style data engineering project that demonstrates a complete modern data stack. It covers the full lifecycle of data: ingestion → streaming → orchestration → storage → transformation → analytics → consumption.

The entire platform is deployed on AWS EC2 (Ubuntu), using Docker for containerization and open-source tools that mirror what real-world data teams use in production.

### 🧰 Tech Stack

LayerTechnologyPurposeInfrastructureDocker, Docker ComposeContainerization & Infrastructure as CodeSource DatabasePostgreSQLRelational source data storeOrchestrationKestraWorkflow scheduling & pipeline automationStreamingApache KafkaReal-time event streamingData LakeMinIOS3-compatible object storageIngestiondlt (data load tool)Automated data loading & schema handlingData WarehouseAmazon Redshift ServerlessCloud-based structured data warehouseTransformationdbt (data build tool)SQL-based analytics engineeringBatch ProcessingApache Spark (PySpark)Distributed batch data processingConsumer LayerStreamlitInteractive business dashboardCloud PlatformAWS EC2 (Ubuntu)Hosting & compute infrastructureLanguagePython, SQLCore scripting & query language

### 📂 Project Structure

nexus-data-platform/
│
├── module1-infra/            # Docker + Postgres + SQL setup
│   ├── docker-compose.yml
│   └── README.md
│
├── module2-kestra/            # Workflow orchestration
│   ├── docker-compose.yml
│   └── README.md
│
├── module7-streaming/          # Kafka + MinIO (streaming & data lake)
│   ├── docker-compose.yml
│   └── README.md
│
├── workshop-dlt/              # Data ingestion pipeline (Postgres → DuckDB / Redshift)
│   ├── pipeline.py
│   └── pipeline_redshift.py
│
├── realtime-pipeline/          # Kafka producer & consumer
│   ├── producer.py
│   └── consumer.py
│
├── module4-dbt/               # dbt project (analytics engineering)
│   └── customer_analytics/
│       └── models/
│           ├── sources.yml
│           └── customer_summary.sql
│
├── module6-spark/              # Batch processing with PySpark
│   └── spark_batch.py
│
├── module8-dashboard/           # Streamlit business dashboard
│   └── dashboard.py
│
├── customers.csv               # Exported sample data
├── orders.csv                  # Exported sample data
└── README.md

### ⚙️ Modules Breakdown

1️⃣ Infrastructure & Source (Docker + Postgres + SQL)

Containerized PostgreSQL database acting as the primary source system, deployed using Docker Compose for reproducible infrastructure.

2️⃣ Workflow Orchestration (Kestra)

Kestra orchestrates and schedules pipeline tasks, connecting to Postgres to trigger and monitor data flows.

3️⃣ Streaming & Data Lake (Kafka + MinIO)

A real-time producer generates order events into a Kafka topic; a consumer reads the stream. MinIO acts as an S3-compatible data lake for raw storage.

4️⃣ Data Ingestion (dlt)

Python-based dlt pipelines extract data from PostgreSQL and load it into destination systems (DuckDB locally, Amazon Redshift in the cloud) with automatic schema handling.

5️⃣ Data Warehouse (Amazon Redshift)

A serverless Redshift workgroup stores structured, query-ready data, loaded via dlt pipelines from both batch and streaming sources.

6️⃣ Analytics Engineering (dbt)

SQL-based dbt models transform raw order and customer data into a business-ready customer_summary view — aggregating total orders, total spend, and average order value per customer.

7️⃣ Batch Processing (Apache Spark)

PySpark reads bulk data via JDBC from PostgreSQL, performs transformations, and writes output in optimized Parquet format.

8️⃣ Consumer Layer (Streamlit Dashboard)

A live, interactive dashboard connected to PostgreSQL, presenting KPIs, revenue breakdowns, top customers, and order distribution — the final business-facing layer of the platform.

### 📊 Dashboard Features

FeatureDescriptionTotal CustomersLive count of all customer recordsTotal OrdersLive count of all order recordsTotal RevenueSum of all order amountsAvg Order ValueMean order value across all ordersRevenue by CustomerBar chart ranking customers by total spendOrders by CityPie chart showing order distribution across citiesFull Data TablesRaw customer and order records in-browser

### 🧠 Key Learnings

Infrastructure as Code using Docker Compose across multiple services
Real-time data streaming with Kafka producer/consumer patterns
Workflow orchestration and cross-container networking with Kestra
Automated data ingestion pipelines using dlt
Cloud data warehousing with Amazon Redshift Serverless
SQL-based analytics engineering with dbt
Distributed batch processing with Apache Spark
Building business-facing dashboards with Streamlit
Real-world troubleshooting: disk space management, Docker daemon recovery, Java/Spark compatibility, AWS networking & security groups

### 📌 Notes


The Redshift Serverless namespace was deleted after development to avoid ongoing cloud costs. Redeploy using the AWS Console and update credentials in pipeline_redshift.py to reactivate this layer.
The EC2 instance can be stopped when not in use; data persists in Docker volumes and restarts automatically on instance start.

### 📄 License

This project is open-source and available for learning purposes under the MIT License.

### 👤 Author

Built as a hands-on data engineering learning project — covering the full modern data stack from ingestion to consumption.
