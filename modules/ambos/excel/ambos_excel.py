import pandas as pd
import io
from openpyxl import Workbook
from modules.ambos.service.ambos_service import AmbosService
from secret.vars_ambiente import DBX_TOKEN
import dropbox
from dropbox.exceptions import DropboxException
from dropbox.files import WriteMode
from messages.responses_ok import ResponseOk


class AmbosExcel:
    @classmethod
    def gerar_excel(cls):
        try:
            result_firestore = AmbosService.get()

            campos_selecionados = ['name', 'local', 'data', 'valor']

            df = pd.DataFrame([{campo: doc[campo] for campo in campos_selecionados} for doc in result_firestore])

            output = io.BytesIO()
            workbook = Workbook()
            sheet = workbook.active
            sheet.append(campos_selecionados)

            for _, row in df.iterrows():
                sheet.append(row.tolist())

            workbook.save(output)
            output.seek(0)

            dbx = dropbox.Dropbox(DBX_TOKEN)
            dbx.files_upload(output.getvalue(), '/Ambos.xlsx', mode=WriteMode.overwrite)

            return ResponseOk.generate_excel_ambos()

        except DropboxException as e:
            print("Erro ao salvar o arquivo no Dropbox:", e)
            return False  # Indica que ocorreu um erro durante o upload
