from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

class RawDataRecord(BaseModel):
    """Data as it comes from a public source."""
    source_id: str
    payload: dict
    extracted_at: datetime = Field(default_factory=datetime.utcnow)

class NormalizedRecord(BaseModel):
    """Standardized shape stored in PostgreSQL."""
    id: str  # Unique hash or deterministic UUID
    source: str
    content: str
    timestamp: datetime
    metadata: dict = {}

    model_config = ConfigDict(from_attributes=True)
