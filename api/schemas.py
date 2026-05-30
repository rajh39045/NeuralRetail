from pydantic import BaseModel


class ChurnRequest(BaseModel):
    recency: float
    frequency: float
    monetary: float
    cluster: int


class SegmentRequest(BaseModel):
    recency: float
    frequency: float
    monetary: float