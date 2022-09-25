import os
from dotenv import load_dotenv

load=load_dotenv()

API_SERVER_URL = os.environ.get('API_SERVER_URL')
URL_PREFIX_DOMAIN= os.environ.get('URL_PREFIX_DOMAIN')
AUTH0_CLIENT_ID= os.environ.get('AUTH0_CLIENT_ID')
API_AUTH0_AUDIENCE= os.environ.get('API_AUTH0_AUDIENCE')
ALGORITHMS= os.environ.get('ALGORITHMS')
AUTH0_DOMAIN= os.environ.get('AUTH0_DOMAIN')
AUTH0_CALLBACK_URL= os.environ.get('AUTH0_CALLBACK_URL')