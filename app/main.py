from fastapi import FastAPI
from app.api import routes, monitoring
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

# Include API routes
app.include_router(routes.router, prefix="/api/v1")
app.include_router(monitoring.router, prefix="/monitor")

@app.on_event("startup")
async def startup_event():
    """
    Startup logic: 
    Could trigger background consumers in future if desired.
    """
    print(f"{settings.PROJECT_NAME} starting up...")

@app.get("/health")
async def health():
    """
    Simple health check.
    """
    return {"status": "online"}
