from fastapi import APIRouter, HTTPException
from app.services.embedding_handler import prompt_query
from app.services.data_store import data_store_instance
from app.models.search import SearchResponse

router = APIRouter()

@router.post("/", response_model= SearchResponse)
async def search_embeddings_endpoint(query: str):
    """
    Busca embeddings para un query dado.
    """
    try:          
        # Genera embeddings para el documento específico
        results = prompt_query(query)
        id = int(results['ids'][0][0].split('--')[0])
        document = data_store_instance.get_data(id)
        title = document['title']
        content_snippet = results['documents'][0][0]
        similarity_score = float(results['distances'][0][0])


        return {"id": id, "title": title, "content_snippet" : content_snippet, "similarity_score": similarity_score }
        
    except HTTPException as http_err:
        raise http_err  # Relanza el error HTTP definido previamente
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")