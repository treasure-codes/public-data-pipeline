from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.models import DataRecordTable  # Hypothetical SQLAlchemy table

async def is_duplicate(session: AsyncSession, record_id: str) -> bool:
    """
    Checks if a record with the same dedupe key already exists in PostgreSQL.
    """
    query = select(DataRecordTable).where(DataRecordTable.id == record_id)
    result = await session.execute(query)
    return result.scalar_one_or_none() is not None
