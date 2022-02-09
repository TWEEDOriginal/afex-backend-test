"""
WSGI config for devtest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

from dotenv import load_dotenv

load_dotenv()
MODE = os.getenv("MODE")

settings_file = "devtest.settings"
if MODE == "DEV":
    settings_file = "devtest.settings.dev"
elif MODE == "STAGING":
    settings_file = "devtest.settings.staging"
elif MODE == "PRODUCTION":
    settings_file = "devtest.settings.production"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_file)

application = get_wsgi_application()
