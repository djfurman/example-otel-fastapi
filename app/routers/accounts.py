import logging

from fastapi import APIRouter, HTTPException
from opentelemetry import trace

tracer = trace.get_tracer_provider().get_tracer(__name__)
router = APIRouter()

accounts = [
    {"id": "abc123", "balance": -500, "isCurrent": True},
    {"id": "def456", "balance": 25, "isCurrent": True},
]


@router.get("/accounts", tags=["accounts"])
async def get_accounts():
    with tracer.start_as_current_span("get_accounts"):
        logging.getLogger().debug("Getting accounts")
        return accounts


@router.get("/accounts/{account_id}", tags=["accounts"])
async def get_account(account_id: str):
    with tracer.start_as_current_span("get_account") as get_account_span:
        logging.getLogger().debug(f"Getting account {account_id}")
        result = [account for account in accounts if account["id"] == account_id]
        if len(result) == 0:
            logging.getLogger().warning(f"Account {account_id} not found")
            get_account_span.set_status(trace.StatusCode.ERROR)
            raise HTTPException(status_code=404, detail="Account not found")
        if len(result) > 1:
            logging.getLogger().error(f"Multiple accounts found for {account_id}")
            get_account_span.set_status(trace.StatusCode.ERROR)
            raise HTTPException(status_code=500, detail="Multiple accounts found")
        get_account_span.set_attribute("account.id", account_id)
        get_account_span.set_status(trace.StatusCode.OK)
        return result[0]
