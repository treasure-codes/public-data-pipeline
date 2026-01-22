from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
async def ping():
    """
    Basic connectivity test endpoint.
    """
    return {"message": "pong"}
