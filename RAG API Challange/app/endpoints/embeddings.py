from fastapi import APIRouter, HTTPException
from app.services.embedding_handler import generate_embeddings
from app.services.data_store import data_store_instance
from typing import Optional


router = APIRouter()

@router.post("/generate-embeddings")
async def generate_embeddings_endpoint(document_id: Optional[int] = None):
    """
    Genera embeddings para un documento específico o para todos los documentos.
    """
    try:
        # Si `document_id` es proporcionado, verifica que el documento existe
        if document_id:
            document = data_store_instance.get_data(document_id)
            if not document:
                raise HTTPException(status_code=404, detail="Documento no encontrado.")
            
            # Genera embeddings para el documento específico
            generate_embeddings(document, document_id)

            return {"message": "Embeddings generados y guardados exitosamente.", "document_id": document_id}
        
        # Si no se proporciona `document_id`, genera embeddings para todos los documentos

        else:
             store = data_store_instance.get_all_data()
             all_documents = [{"id": doc_id, **doc_data} for doc_id, doc_data in store.items()]
             if not all_documents:
                 raise HTTPException(status_code=404, detail="No hay documentos para procesar.")

             # Genera y guarda embeddings para todos los documentos
             
             for doc in all_documents:
            # Genera embeddings basados en el ID del documento
                 document = data_store_instance.get_data(doc['id'])
                 generate_embeddings(document, doc["id"])


             return {"message": "Embeddings generados y guardados exitosamente para todos los documentos."}

    except HTTPException as http_err:
        raise http_err  # Relanza el error HTTP definido previamente
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")