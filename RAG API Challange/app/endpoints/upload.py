from fastapi import APIRouter, HTTPException
from app.services.data_store import data_store_instance
from app.models.upload import UploadData, UploadResponse

router = APIRouter()


@router.post("/", response_model=UploadResponse)
async def upload_data(data: UploadData):
    try:
        document_id = data_store_instance.save_data(data.title, data.content)
        return {"message": "Datos guardados correctamente", "id": document_id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/documents/{document_id}")
async def get_document(document_id: int):
    document = data_store_instance.get_data(document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Documento no encontrado")
    return document


@router.get("/documents/")
async def get_documents():
    documents = data_store_instance.get_all_data()

    if not documents:
        # Devuelve un resultado vacío en lugar de lanzar una excepción
        return {"message": "No hay documentos disponibles", "documents": []}

    # Devuelve los documentos como una lista de objetos con IDs y datos
    return [{"id": doc_id, **doc_data} for doc_id, doc_data in documents.items()]