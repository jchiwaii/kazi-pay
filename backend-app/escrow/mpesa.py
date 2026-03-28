import base64
from datetime import datetime
from authApp.utils import DarajaClient
from django.conf import settings
import requests

class MpesaC2B(DarajaClient):
    def stk_push(self, phone, amount, reference):
        token = self.get_token()
        url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        # Password is Base64(BusinessShortCode + Passkey + Timestamp)
        data_to_encode = settings.MPESA_SHORTCODE + settings.MPESA_PASSKEY + timestamp
        password = base64.b64encode(data_to_encode.encode()).decode('utf-8')

        payload = {
            "BusinessShortCode": settings.MPESA_SHORTCODE,
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": int(amount),
            "PartyA": phone, # 2547xxxxxxxx
            "PartyB": settings.MPESA_SHORTCODE,
            "PhoneNumber": phone,
            "CallBackURL": settings.MPESA_C2B_CALLBACK_URL,
            "AccountReference": reference,
            "TransactionDesc": "Kazipesa Escrow Deposit"
        }
        
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.post(url, json=payload, headers=headers)
        return response.json()