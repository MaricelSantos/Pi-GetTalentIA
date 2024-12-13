from config.config import cohere_client
from app.services.embedding_handler import prompt_query

def RAG_answer(question):

    prompt_identificacion = f""" 
            La PREGUNTA puede responderse utilizando el CONTEXTO?.
            Debes responder unicamente 'SI' o 'NO'
            
            ###
            CONTEXTO:
            {prompt_query(question)}

            ###
            PREGUNTA:
            {question}

            ###
            Respuesta:
            
            """

    system_identificacion = "Actua como un analizador de contexto. Solo debes responder con monosilabos, responder SI o NO"


    response = cohere_client.chat(
        model="command-r-plus-08-2024",
        messages=[{"role": "system", "content": system_identificacion},
                 {"role": "user", "content": prompt_identificacion}],
    )

    respuesta_al_usuario = response.message.content[0].text
    

    if 'SI' in respuesta_al_usuario:

        prompt_principal = f""" 
            Responde la pregunta siguiendo las instrucciones y basandote en la informacion brindada por el contexto.
            
            ###
            Instrucciones: 
            -Responde la pregunta para un niño.

            ###
            Contexto:
            {prompt_query(question)}

            ###
            Pregunta:
            {question}

            ###
            Respuesta:
            
            """

        system_prompt_principal = "Tu tarea es responder la pregunta utilizando el contexto brindado como fuente de informacion."
        response = cohere_client.chat(
            model="command-r-plus-08-2024",
            messages=[{"role": "system", "content": system_prompt_principal},
                     {"role": "user", "content": prompt_principal}],
                        )
        
        respuesta_al_usuario = response.message.content[0].text

    else:
       respuesta_al_usuario = 'Lo siento no tengo información sobre lo que me preguntas'
    

    return respuesta_al_usuario