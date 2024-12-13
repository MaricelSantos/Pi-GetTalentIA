from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_text(text):
    """
    Divide un texto en fragmentos de tamaño definido.
    """
    #Configuración del text_splitter: utilizo el atributo separators para que más alla del chunk size respete las estructuras
    #                                 oraciones de forma tal de no perder contexto  
    # El chunk size respeta por regla simple que va haber siempre menos de 512 token
    # Regla simple (4 caracteres = 1 token). Si coloco un número menor separa los titulos del primer parrafo
    text_splitter = RecursiveCharacterTextSplitter(separators = [ "."], 
                                               chunk_size=550, 
                                               chunk_overlap=0,
                                               length_function = len)
           
                                              

    # Dividir el texto en párrafos
    return text_splitter.split_text(text)

