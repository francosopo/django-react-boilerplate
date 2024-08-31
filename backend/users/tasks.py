from django.core import management

<<<<<<< HEAD
from explora_uchile_backend import celery_app
=======
from {{project_name}} import celery_app
>>>>>>> 37cb4d29a35886fe431d5797246534db912e0cc2


@celery_app.task
def clearsessions():
    management.call_command("clearsessions")
