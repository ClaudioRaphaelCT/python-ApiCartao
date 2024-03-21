from database.connection import get_docs_ambos


class AmbosService:
    @classmethod
    def get(cls):
        database = []
        docs = get_docs_ambos()
        for doc in docs:
            doc_data = doc.to_dict()
            doc_data['id'] = doc.id
            database.append(doc_data)
        return database
