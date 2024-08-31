from django.core import management

from explora_uchile_backend import celery_app


@celery_app.task
def clearsessions():
    management.call_command("clearsessions")
