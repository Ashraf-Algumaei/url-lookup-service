from pydantic import BaseModel
from typing import Optional


class UrlInsertResponse(BaseModel):
    status: Optional[str] = "Success"
