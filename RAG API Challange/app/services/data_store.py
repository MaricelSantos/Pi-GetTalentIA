class DataStore:
    def __init__(self):
        self.data_store = {}  # Diccionario para almacenar los datos
        self.id_counter = 1   # Contador global para los IDs únicos

    def save_data(self, title, content):
        # Verifica si el título ya existe
        if any(d["title"] == title for d in self.data_store.values()):
            raise ValueError("El título ya existe.")

        if not isinstance(title, str) or len(title) == 0:
            raise ValueError("Debes dar un título en formato str")

        if not isinstance(content, str) or len(content) == 0:
            raise ValueError("Debes dar un contenido en formato str")


        # Asigna un nuevo ID y guarda los datos
        document_id = self.id_counter
        self.data_store[document_id] = {"title": title, "content": content}
        self.id_counter += 1

        return document_id

    def get_data(self, document_id):
        # Obtiene un documento específico
        return self.data_store.get(document_id)

    def get_all_data(self):
        # Retorna todos los documentos
        return self.data_store

    def delete_data(self, document_id):
        # Elimina un documento por su ID
        if document_id in self.data_store:
            del self.data_store[document_id]
        else:
            raise ValueError("El documento no existe.")

# Instancia Singleton de DataStore
data_store_instance = DataStore()
