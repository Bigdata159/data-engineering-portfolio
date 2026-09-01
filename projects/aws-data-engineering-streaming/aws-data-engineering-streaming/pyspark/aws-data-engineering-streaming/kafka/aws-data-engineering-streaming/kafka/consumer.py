from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "customer-events",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda value: json.loads(
        value.decode("utf-8")
    ),
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="data-engineering-group"
)

for message in consumer:

    event = message.value

    print(
        f"Customer: {event['customer_id']} | "
        f"Event: {event['event']} | "
        f"Amount: {event['amount']}"
    )
