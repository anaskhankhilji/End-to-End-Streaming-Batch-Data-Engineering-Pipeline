import json
from kafka import KafkaConsumer

def safe_deserialize(v):
    if v is None:
        return None
    try:
        return json.loads(v.decode('utf-8'))
    except Exception:
        return None

consumer = KafkaConsumer(
    'orders',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=safe_deserialize
)

print("Consumer shuru ho gaya... naye orders sun raha hai")

try:
    for message in consumer:
        order = message.value
        if order is None:
            continue
        print(f"Received: Order #{order['order_id']} | {order['customer']} | ${order['amount']} | {order['city']}")
except KeyboardInterrupt:
    print("Consumer band ho gaya.")
