from pydantic import BaseModel, Field
from typing import List, Optional


class UrlInsertRequest(BaseModel):
    urls: Optional[List[str]] = Field(None, example=["sampleurl.com", "sampleurl2.com"], min_items=1)
