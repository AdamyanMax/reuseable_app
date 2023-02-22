# mylibrary/wsgi.py

import os

from django.core.wsgi import get_wsgi_application


def create_app():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reusable_app.settings')
    app = get_wsgi_application()
    return app
