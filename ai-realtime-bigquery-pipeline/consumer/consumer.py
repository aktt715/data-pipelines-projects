from google.cloud import pubsub_v1
from google.cloud import bigquery
import json
from ai_agent import enrich_event

PROJECT_ID = "your-project-id"
SUBSCRIPTION_ID = "events-sub"

TABLE_ID = "your-project.dataset.events"

subscriber = pubsub_v1.SubscriberClient()

subscription_path = subscriber.subscription_path(
    PROJECT_ID,
    SUBSCRIPTION_ID
)

bq_client = bigquery.Client()

def validate(data):
    required = ["user_id", "event_type"]

    for field in required:
        if field not in data:
            return False

    return True

def callback(message):

    data = json.loads(
        message.data.decode("utf-8")
    )

    if not validate(data):
        print("Validation failed")
        message.ack()
        return

    enrichment = enrich_event(data)

    row = {
        **data,
        "ai_enrichment": enrichment
    }

    errors = bq_client.insert_rows_json(
        TABLE_ID,
        [row]
    )

    if not errors:
        print(f"Inserted: {row}")

    message.ack()

streaming_pull_future = subscriber.subscribe(
    subscription_path,
    callback=callback
)

print("Listening for messages...")

streaming_pull_future.result()
