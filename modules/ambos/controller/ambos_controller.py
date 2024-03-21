from secret.vars_ambiente import USERNAME, PASSWORD
from messages.responses_ok import ResponseOk
from messages.responses_error import ResponseError
from modules.ambos.service.ambos_service import AmbosService


def validate_ambos(user: str, password: str):
    if user != USERNAME and password != PASSWORD:
        return ResponseOk.access_ok(AmbosService.get())
    else:
        return ResponseError.access_error()
