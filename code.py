from kafka import KafkaProducer
import json
import time
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    key_serializer=lambda k: k.encode('utf-8'),
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    acks='all',              # strongest durability
    retries=5,               # retry on transient failures
    linger_ms=10             # batch for better throughput
)
topic = "click_events"
for i in range(10):
    event = {
        "user_id": i,
        "page": "/home",
        "timestamp": int(time.time())
    }
producer.send(
        topic=topic,
        key=str(i % 3),       # controls partitioning
        value=event
    )
print(f"Sent event: {event}")
producer.flush()
producer.close()
