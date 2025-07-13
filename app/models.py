from pydantic import BaseModel


class Account(BaseModel):
    id: str
    is_current: bool
    balance: float
