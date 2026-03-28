from django.conf import settings
from django.db import models

class WorkerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    skills = models.TextField()
    experience = models.TextField()

    def __str__(self):
        return self.user.username


class WorkerRating(models.Model):
    worker = models.ForeignKey(WorkerProfile, on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField()
    feedback = models.TextField(blank=True)

    def __str__(self):
        return f"Rating for {self.worker.user.username}: {self.rating}" 

class Bid(models.Model):
    job = models.ForeignKey('clients.Job', on_delete=models.CASCADE, related_name='bids')
    worker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bids_placed')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    proposal = models.TextField() # Why should the client pick them?
    is_accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('job', 'worker')