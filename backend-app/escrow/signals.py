from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Job
from notification.utils import send_kazi_sms

@receiver(post_save, sender=Job)
def notify_job_status_change(sender, instance, created, **kwargs):
    # 1. When Client pays (Funds enter Escrow)
    if instance.status == 'PAID':
        if instance.worker:
            message = (
                f"Kazi-Pay: Funds for '{instance.title}' (KES {instance.amount}) "
                f"are now in Escrow. You can start the work! "
                f"Dial *384*23550# when finished."
            )
            send_kazi_sms(instance.worker.phone_number, message)

    # 2. When Worker marks as Done (Notify Client)
    elif instance.status == 'UNDER_REVIEW':
        message = (
            f"Kazi-Pay: Worker {instance.worker.username} has finished '{instance.title}'. "
            f"Please dial *384*23550# to approve and release the KES {instance.amount}."
        )
        send_kazi_sms(instance.client.phone_number, message)

    # 3. When Payment is Released (Notify Worker)
    elif instance.status == 'COMPLETED':
        message = (
            f"Kazi-Pay: Payment of KES {instance.amount} for '{instance.title}' "
            f"has been released to your M-Pesa. Thank you for using Kazi-Pay!"
        )
        send_kazi_sms(instance.worker.phone_number, message)