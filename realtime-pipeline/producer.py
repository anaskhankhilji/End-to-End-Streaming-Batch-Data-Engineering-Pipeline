import json
import time
import random
from kafka import KafkaProducer
from faker import Faker

fake = Faker()

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

order_id = 1

print("Producer shuru ho gaya... Ctrl+C se rukein")

try:
    while True:
        order = {
            "order_id": order_id,
            "customer": fake.name(),
            "amount": round(random.uniform(10, 1000), 2),
            "city": fake.city(),
            "timestamp": time.time()
        }
        producer.send('orders', value=order)
        print(f"Sent: {order}")
        order_id += 1
        time.sleep(2)  # har 2 second mein ek naya order
except KeyboardInterrupt:
    print("Producer band ho gaya.")
    producer.close()
