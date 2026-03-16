from fastapi import FastAPI

from infrastructure.api.reservation_router import router as reservation_router
from infrastructure.database.connection import lifespan

app = FastAPI(lifespan=lifespan)
app.include_router(reservation_router)


@app.get("/health")
async def health():
    return {"status": "ok"}
