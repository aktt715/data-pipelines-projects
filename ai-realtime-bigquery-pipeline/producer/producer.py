from google.cloud import pubsub_v1
import json
import time
import random

PROJECT_ID = "your-project-id"
TOPIC_ID = "events-topic"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

EVENTS = ["login", "purchase", "logout", "search"]

while True:
    event = {
        "user_id": random.randint(1, 1000),
        "event_type": random.choice(EVENTS),
        "amount": random.randint(10, 500),
        "timestamp": time.time()
    }

    data = json.dumps(event).encode("utf-8")
    publisher.publish(topic_path, data)

    print(f"Published: {event}")

    time.sleep(2)
