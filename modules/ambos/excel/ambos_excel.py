import pandas as pd
import os
from openpyxl import Workbook
from modules.ambos.service.ambos_service import AmbosService
from messages.responses_ok import ResponseOk
from secret.vars_ambiente import DIRECTORY


class AmbosExcel:
    @classmethod
    def gerar_excel(cls):
        result_firestore = AmbosService.get()

        campos_selecionados = ['name', 'local', 'data', 'valor']

        df = pd.DataFrame([{campo: doc[campo] for campo in campos_selecionados} for doc in result_firestore])

        workbook = Workbook()
        sheet = workbook.active

        sheet.append(campos_selecionados)

        for _, row in df.iterrows():
            sheet.append(row.tolist())

        caminho_arquivo = os.path.join(DIRECTORY, "Ambos.xlsx")
        workbook.save(caminho_arquivo)
        return ResponseOk.generate_excel_ambos()


