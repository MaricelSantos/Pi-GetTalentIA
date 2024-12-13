from app.services.chunker import chunk_text
from config.config import cohere_client
import chromadb 
from chromadb import Documents, EmbeddingFunction, Embeddings


chroma_client = chromadb.Client()

# Define el directorio donde deseas almacenar la colección
#persist_directory = "../db/collections"

    

# Define la función para obtener embeddings de Cohere
def get_embeddings(text):
    """
    Funcion para generar embeddings.
    """
    response = cohere_client.embed(
        texts=text,
        model="embed-multilingual-v3.0", #Este modelo es el de mayor dimension entre los multilingüe y el de mayor numero de tokens
        input_type="search_document",
        embedding_types=["float"],
    )
    return response.embeddings.float_  # Cohere devuelve embeddings como una lista de listas


# Crea la clase personalizada de EmbeddingFunction para ChromaDB
class MyEmbeddingFunction(EmbeddingFunction):
    def __call__(self, input: Documents) -> Embeddings:
        # Llama a la función de Cohere para obtener las embeddings
        return get_embeddings(input)  # input es una lista de textos

# Creo la coleccion
# Crea una colección usando la función de embeddings personalizada
collection = chroma_client.get_or_create_collection(name="historias_fragmentadas",
                                      embedding_function=MyEmbeddingFunction()
                                     )


def generate_embeddings(document_data=None, document_id= None):
    """
    Función para almacenar embeddings.
    Si se proporciona un `document_id`, solo genera embeddings para ese documento.
    Si no, genera embeddings para todos los documentos.
    """
    
    content = document_data['content']
    
    # Divide el contenido en fragmentos (chunks)
    chunks = chunk_text(content)
        
    # Obtén los embeddings para los fragmentos de texto
    collection.add(
        documents=chunks,
        ids= [f"{document_id}--fragmento{i}" for i in range(len(chunks))]
    )
    
def prompt_query(prompt):
    results = collection.query(
        query_texts= prompt,  # Pasamos el prompt
        n_results=3  # Número de resultados a retornar
    )
    return results





