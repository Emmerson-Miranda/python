from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    x: int
    y: int
    result: Optional[int] = None
