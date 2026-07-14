import os
import sys
from django.core.wsgi import get_wsgi_application

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, ROOT_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LGM.settings')
application = get_wsgi_application()
