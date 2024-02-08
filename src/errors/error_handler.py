from src.views.http_types.http_response import HttpResponse
from .error_types.http_unprocessable_entity import HttpUnprocessableEntityErro

def handler_errors(error: Exception):
    if isinstance(error, HttpUnprocessableEntityErro):
        # enviar para um log
        # enviar um email de notificacao
        return HttpResponse(
            status_code=error.status_code,
            body={
                "erros": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )

    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Server Error",
                "detail": str(error)

            }]
        }
    )
