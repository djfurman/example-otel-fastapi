from fastapi import FastAPI

from .routers import accounts

app = FastAPI()


app.include_router(accounts.router)


@app.get("/health")
async def get_health_status():
    return {"isHealthy": True}
