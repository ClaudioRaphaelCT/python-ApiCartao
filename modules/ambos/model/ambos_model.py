from pydantic import BaseModel


class AmbosModel(BaseModel):
    user: str
    password: str
