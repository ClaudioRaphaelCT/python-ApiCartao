from starlette.responses import JSONResponse


class ResponseError:
    @classmethod
    def access_error(cls):
        return JSONResponse(status_code=404, content={"message": "Usuario e/ou senha incorreto(s)"})
