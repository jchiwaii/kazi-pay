from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Notification
from .serializers import NotificationSerializer
from authApp.models import CustomUser  # Ensure this path is correct

class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user)
    
    @action(detail=True, methods=['post'])
    def mark_as_read(self, request, pk=None):
        notif = self.get_object()
        notif.is_read = True
        notif.save()
        return Response({"status": "read"})

#  AFRICA'S TALKING (USSD/SMS) 

@csrf_exempt
def ussd_callback(request):
    """
    Handles the USSD logic for *384*23550#
    """
    if request.method == 'POST':
        session_id = request.POST.get("sessionId")
        service_code = request.POST.get("serviceCode")
        phone_number = request.POST.get("phoneNumber")
        text = request.POST.get("text", "")

        response = ""

        # Main Menu
        if text == "":
            try:
                # Try to find user by phone number
                user = CustomUser.objects.get(phone_number=phone_number)
                response = f"CON Welcome {user.username} to Kazi-Pay\n"
                response += "1. Search for Jobs\n"
                response += "2. Check Escrow Balance\n"
                response += "3. My Active Jobs"
            except CustomUser.DoesNotExist:
                response = "CON Welcome to Kazi-Pay\n"
                response += "1. Register as Worker\n"
                response += "2. Register as Client\n"
                response += "3. About Us"

        # Logic for "Search for Jobs" or "Register as Worker"
        elif text == "1":
            response = "CON Select Category:\n1. Plumbing\n2. Electrical\n3. Cleaning"
            
        elif text == "1*1":
            response = "END Looking for Plumbing jobs near you. We will SMS you when one is found!"

        # Logic for Balance
        elif text == "2":
            response = "END Your Kazi-Pay Escrow balance is KES 0.00"

        else:
            response = "END Invalid option. Please try again."

        return HttpResponse(response, content_type='text/plain')
    
    return HttpResponse("USSD Endpoint", status=400)

@csrf_exempt
def sms_callback(request):
    """
    Handles inbound SMS sent to shortcode 23440
    """
    if request.method == 'POST':
        # logic for processing incoming SMS
        return HttpResponse("OK", status=200)
    return HttpResponse("Method not allowed", status=405)