from fastapi import APIRouter, HTTPException
from app.services.RAG_answer import RAG_answer
from app.services.data_store import data_store_instance


router = APIRouter()

@router.post("/")
async def RAG_answer_endpoint(query: str):
    """
    Conecta con LLM y genera respuesta.
    """
    try:          
        # Genera embeddings para el documento específico
        response = RAG_answer(query)
   
        return {"pregunta": query, "respuesta": response }
        
        # Si no se proporciona `document_id`, genera embeddings para todos los documentos
        # TODO
        # else:
        #     all_documents = data_store_instance.get_all_data()
        #     if not all_documents:
        #         raise HTTPException(status_code=404, detail="No hay documentos para procesar.")

        #     # Genera y guarda embeddings para todos los documentos
        #     for doc_id in all_documents.keys():
        #     # Genera embeddings basados en el ID del documento
        #         embeddings = generate_embeddings(document_id=doc_id)
        #         save_embeddings(document_id=doc_id, embeddings=embeddings)

        #     return {"message": "Embeddings generados y guardados exitosamente para todos los documentos."}

    except HTTPException as http_err:
        raise http_err  # Relanza el error HTTP definido previamente
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")