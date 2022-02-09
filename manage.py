#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv

load_dotenv()
MODE = os.getenv("MODE")


def main():
    settings_file = "devtest.settings"
    if MODE == "DEV":
        settings_file = "devtest.settings.dev"
    elif MODE == "STAGING":
        settings_file = "devtest.settings.staging"
    elif MODE == "PRODUCTION":
        settings_file = "devtest.settings.production"

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_file)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
