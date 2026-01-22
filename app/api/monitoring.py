from fastapi import APIRouter
from app.services.kafka_client import KafkaManager

router = APIRouter()

@router.get("/status")
async def pipeline_status():
    """
    Returns a mock pipeline status.
    In production, you'd return Kafka consumer lag, DB stats, etc.
    """
    status = {
        "pipeline": "active",
        "kafka_topic": "web_data_raw",
        "pending_messages": 42,  # Example static number
        "consumers": 1
    }
    return status
