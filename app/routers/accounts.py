from fastapi import APIRouter

router = APIRouter()


@router.get("/accounts", tags=["accounts"])
async def get_accounts():
    return {
        "accounts": [
            {"id": "abc123", "balance": -500, "isCurrent": True},
            {"id": "def456", "balance": 25, "isCurrent": True},
        ]
    }


@router.get("/accounts/{account_id}", tags=["accounts"])
async def get_account(account_id: str):
    return {"id": account_id, "balance": -500, "isCurrent": True}
