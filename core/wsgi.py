import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')  # Certifique-se de que 'core.settings' está correto

application = get_wsgi_application()
