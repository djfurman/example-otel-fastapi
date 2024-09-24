from fastapi import FastAPI
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

COLLECTOR_ENDPOINT = "https://api.honeycomb.io"
resource = Resource(attributes={"service.name": "fastapi-demo"})
provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(OTLPSpanExporter(endpoint=COLLECTOR_ENDPOINT))
provider.add_span_processor(processor)

trace.set_tracer_provider(provider)

app = FastAPI()
FastAPIInstrumentor().instrument_app(app)

@app.get("/health")
def get_health_status():
    return {"isHealthy": True}
