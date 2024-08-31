#!/usr/bin/env python

import os
import sys

from decouple import config


if __name__ == "__main__":
    settings_module = config("DJANGO_SETTINGS_MODULE", default=None)

    if sys.argv[1] == "test":
        if settings_module:
            print(
                "Ignoring config('DJANGO_SETTINGS_MODULE') because it's test. "
<<<<<<< HEAD
                "Using 'explora_uchile_backend.settings.test'"
            )
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "explora_uchile_backend.settings.test")
=======
                "Using '{{project_name}}.settings.test'"
            )
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{project_name}}.settings.test")
>>>>>>> 37cb4d29a35886fe431d5797246534db912e0cc2
    else:
        if settings_module is None:
            print(
                "Error: no DJANGO_SETTINGS_MODULE found. Will NOT start devserver. "
                "Remember to create .env file at project root. "
                "Check README for more info."
            )
            sys.exit(1)
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
