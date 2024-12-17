from typing import Any, Dict
from pydantic import BaseModel


class LogData(BaseModel):
    message: str
    metadata: Dict[str, Any] = {}
