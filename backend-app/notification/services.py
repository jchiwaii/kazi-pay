from .models import Notification

class NotificationService:
    @staticmethod
    def send(recipient, title, message, link=None):
        return Notification.objects.create(
            recipient=recipient,
            title=title,
            message=message,
            link=link
        )