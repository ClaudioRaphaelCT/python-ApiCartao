class ResponseOk:
    @classmethod
    def access_ok(cls, database):
        return {"Ambos": database}

    @classmethod
    def generate_excel_ambos(cls):
        return {"status": "Excel gerado", "Excel": "Ambos"}
