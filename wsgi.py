import os
import sys

# Adicione o diretório do seu projeto ao caminho do sistema
path = '/home/jefinhojz/API_Pontos_de_Interesse_por_GPS'  # Atualize este caminho para o diretório do seu projeto Django
if path not in sys.path:
    sys.path.append(path)

# Configure as variáveis de ambiente para o seu projeto Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'

# Obtenha a aplicação WSGI do Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
