import asyncio
from datetime import datetime
from app.services.kafka_client import KafkaManager
from app.models.records import RawDataRecord
import random

async def fetch_public_data():
    """
    Simulates fetching data from a public source.
    Replace with real APIs later if needed.
    """
    sample_data = [
        {"title": "News A", "description": "Lorem ipsum A"},
        {"title": "News B", "description": "Lorem ipsum B"},
        {"title": "News C", "description": "Lorem ipsum C"},
    ]
    return [
        RawDataRecord(
            source_id=f"mock_source_{i}",
            payload=item,
            extracted_at=datetime.utcnow()
        )
        for i, item in enumerate(sample_data)
    ]

async def produce_to_kafka(records):
    producer = await KafkaManager.get_producer()
    for record in records:
        await producer.send_and_wait(settings.KAFKA_TOPIC_RAW, record.dict())
        print(f"Sent record {record.source_id} to Kafka")

async def main():
    while True:
        records = await fetch_public_data()
        await produce_to_kafka(records)
        await asyncio.sleep(5)  # Wait before fetching next batch

if __name__ == "__main__":
    asyncio.run(main())
