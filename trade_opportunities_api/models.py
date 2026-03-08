from pydantic import BaseModel

class SectorRequest(BaseModel):
    sector: str


