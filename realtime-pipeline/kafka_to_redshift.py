import json
import dlt
from kafka import KafkaConsumer

def safe_deserialize(v):
    if v is None:
        return None
    try:
        return json.loads(v.decode('utf-8'))
    except Exception:
        return None

# Kafka se saara data padho (shuru se)
consumer = KafkaConsumer(
    'orders',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=safe_deserialize,
    consumer_timeout_ms=5000  # 5 second baad ruk jayega agar naya data na aaye
)

orders = []
for message in consumer:
    if message.value is not None:
        orders.append(message.value)

print(f"Total {len(orders)} orders Kafka se collect hue.")

# Redshift mein load karo
pipeline = dlt.pipeline(
    pipeline_name="kafka_orders_pipeline",
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

load_info = pipeline.run(orders, table_name="orders")
print(load_info)
