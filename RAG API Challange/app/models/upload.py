from pydantic import BaseModel

# Modelos de entrada y salida
class UploadData(BaseModel):
    title: str
    content: str

class UploadResponse(BaseModel):
    message: str
    id: int
