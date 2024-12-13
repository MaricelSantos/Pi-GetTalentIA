from pydantic import BaseModel
from typing import Optional


class SearchResponse(BaseModel):
    id: int
    title : str
    content_snippet: str
    similarity_score: Optional[float] = None