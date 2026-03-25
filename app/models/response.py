from pydantic import BaseModel

class DataResponse(BaseModel):
    source: str
    data: str
