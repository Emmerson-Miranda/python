from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    """
    Class used as parameter for operations like addition, multiply...
    """
    x: int
    y: int
    result: Optional[int] = None
