from llama_index.core.storage.storage_context import StorageContext
from llama_index.core import load_index_from_storage

class Serene():
    def __init__(self):
        pass

    def make_prediction(self, content):
        response =  self.answerMe(content)
        return response.response
    
    def answerMe(self, content):
        storage_context = StorageContext.from_defaults(persist_dir = 'SERENESOUL/static/Store')
        index = load_index_from_storage(storage_context)
        query_engine = index.as_query_engine()
        response = query_engine.query(content)
        return response