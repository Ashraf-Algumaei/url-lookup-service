from pydantic import BaseModel, Field
from typing import Optional


class UrlLookupResponse(BaseModel):
    hostName: Optional[str] = Field(None, example="test-hostname.com")
    status: Optional[str] = Field(None, example="MALWARE")
