import json
import logging
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
from app.core.config import settings

logger = logging.getLogger(__name__)

class KafkaManager:
    _producer: AIOKafkaProducer = None

    @classmethod
    async def get_producer(cls) -> AIOKafkaProducer:
        if cls._producer is None:
            cls._producer = AIOKafkaProducer(
                bootstrap_servers=settings.KAFKA_BROKER_URL,
                value_serializer=lambda v: json.dumps(v).encode("utf-8")
            )
            await cls._producer.start()
        return cls._producer

    @classmethod
    def get_consumer(cls, topic: str) -> AIOKafkaConsumer:
        return AIOKafkaConsumer(
            topic,
            bootstrap_servers=settings.KAFKA_BROKER_URL,
            group_id="normalization-group",
            value_deserializer=lambda m: json.loads(m.decode("utf-8")),
            auto_offset_reset="earliest"
        )
