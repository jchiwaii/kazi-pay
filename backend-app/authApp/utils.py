import requests
from requests.auth import HTTPBasicAuth
from django.conf import settings
from datetime import datetime

class DarajaClient:
    def __init__(self):
        self.consumer_key = settings.MPESA_CONSUMER_KEY
        self.consumer_secret = settings.MPESA_CONSUMER_SECRET
        self.auth_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    def get_token(self):
        res = requests.get(self.auth_url, auth=HTTPBasicAuth(self.consumer_key, self.consumer_secret))
        return res.json().get('access_token')