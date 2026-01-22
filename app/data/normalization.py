import hashlib
from app.models.records import RawDataRecord, NormalizedRecord

class Normalizer:
    @staticmethod
    def generate_dedupe_key(source_id: str, payload: dict) -> str:
        """
        Creates a unique hash based on source_id and payload.
        This prevents duplicate records.
        """
        hash_input = f"{source_id}:{str(sorted(payload.items()))}"
        return hashlib.sha256(hash_input.encode()).hexdigest()

    @classmethod
    def process(cls, raw: RawDataRecord) -> NormalizedRecord:
        """
        Transforms raw data into normalized format.
        """
        return NormalizedRecord(
            id=cls.generate_dedupe_key(raw.source_id, raw.payload),
            source=raw.source_id,
            content=raw.payload.get("text") or raw.payload.get("description", ""),
            timestamp=raw.extracted_at,
            metadata={"original_keys": list(raw.payload.keys())}
        )
