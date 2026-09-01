from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda value: json.dumps(value).encode("utf-8")
)

events = [
    {
        "customer_id": 101,
        "event": "purchase",
        "amount": 500
    },
    {
        "customer_id": 102,
        "event": "purchase",
        "amount": 750
    },
    {
        "customer_id": 103,
        "event": "login",
        "amount": 0
    }
]

for event in events:
    producer.send("customer-events", event)
    print(f"Sent: {event}")
    time.sleep(1)

producer.flush()
producer.close()
