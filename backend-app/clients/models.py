from django.conf import settings
from django.db import models

class ClientProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Job(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('completed_by_worker', 'Waiting for Client Approval'), # New status
        ('completed', 'Finalized'),
        ('cancelled', 'Cancelled'),
    )
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    assigned_worker = models.ForeignKey('workers.WorkerProfile', null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='open')

    def __str__(self):
        return self.title

class JobRequirement(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='requirements')
    requirement = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.job.title} - {self.requirement}"

class ClientRating(models.Model):
    job = models.OneToOneField(Job, on_delete=models.CASCADE, related_name='client_rating')
    rating = models.IntegerField()
    feedback = models.TextField(blank=True)

    def __str__(self):
        return f"Rating for {self.job.title}: {self.rating}"