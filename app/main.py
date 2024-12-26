import logging

from fastapi import FastAPI
from opentelemetry import trace

from .routers import accounts

tracer = trace.get_tracer_provider().get_tracer(__name__)
app = FastAPI()


app.include_router(accounts.router)


@app.get("/health")
async def get_health_status():
    with tracer.start_as_current_span("get_health_status"):
        logging.getLogger().debug("Health check completed")
        return {"isHealthy": True}
