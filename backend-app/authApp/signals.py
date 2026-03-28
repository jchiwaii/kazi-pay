from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'worker':
            from workers.models import WorkerProfile
            WorkerProfile.objects.create(user=instance)
            
        elif instance.role == 'client':
            from clients.models import ClientProfile
            ClientProfile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    if instance.role == 'worker' and hasattr(instance, 'workerprofile'):
        instance.workerprofile.save()
    elif instance.role == 'client' and hasattr(instance, 'clientprofile'):
        instance.clientprofile.save()