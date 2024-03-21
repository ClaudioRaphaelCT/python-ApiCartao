from fastapi import FastAPI
from modules.ambos.model.ambos_model import AmbosModel
from modules.ambos.controller.ambos_controller import validate_ambos
from modules.ambos.excel.ambos_excel import AmbosExcel

app = FastAPI(title="Uso do cartão")


@app.get("/")
def home():
    return {"swagger": "/docs"}


@app.get("/ambos")
def get_ambos(ambos: AmbosModel):
    return validate_ambos(ambos.user, ambos.password)


@app.get("/ambos/excel")
def get_ambos_excel():
    return AmbosExcel.gerar_excel()
