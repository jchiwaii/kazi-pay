from authApp.utils import DarajaClient
from django.conf import settings
import requests

class MpesaB2C(DarajaClient):
    def pay_worker(self, phone, amount, remark):
        token = self.get_token()
        url = "https://sandbox.safaricom.co.ke/mpesa/b2c/v3/paymentrequest"
        
        payload = {
            "InitiatorName": settings.MPESA_INITIATOR_NAME,
            "SecurityCredential": settings.MPESA_SECURITY_CREDENTIAL,
            "CommandID": "BusinessPayment",
            "Amount": int(amount),
            "PartyA": settings.MPESA_SHORTCODE,
            "PartyB": phone,
            "Remarks": remark,
            "QueueTimeOutURL": settings.MPESA_B2C_TIMEOUT_URL,
            "ResultURL": settings.MPESA_B2C_CALLBACK_URL,
            "Occasion": "GigPayout",
            "OriginatorConversationID": f"payout_{phone}_{amount}"
        }
        
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.post(url, json=payload, headers=headers)
        return response.json()