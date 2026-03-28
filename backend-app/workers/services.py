from django.db import transaction
from django.core.exceptions import ValidationError
from .models import Bid
from clients.models import Job
from notification.services import NotificationService

class WorkerService:
    @staticmethod
    @transaction.atomic
    def place_bid(worker, job_id, amount, proposal):
        """
        Logic to place a bid on an open job.
        Ensures the worker isn't bidding on their own job or a closed job.
        """
        job = Job.objects.get(id=job_id)
        
        if job.status != 'open':
            raise ValidationError("This job is no longer open for bidding.")
        
        if job.client == worker:
            raise ValidationError("You cannot bid on your own job.")

        # Check if worker already bid (handled by unique_together, but good for UX)
        if Bid.objects.filter(job=job, worker=worker).exists():
            raise ValidationError("You have already placed a bid on this job.")

        bid = Bid.objects.create(
            job=job,
            worker=worker,
            amount=amount,
            proposal=proposal
        )
        return bid

    @staticmethod
    def complete_job(worker, job):
        """
        Logic for a worker to signal that they have finished the work.
        This changes the job status so the client can approve/release escrow.
        """
        if job.assigned_worker != worker:
            raise ValidationError("You are not the assigned worker for this job.")
        
        if job.status != 'in_progress':
            raise ValidationError("Job must be 'in_progress' to be marked as complete.")

        # We update the status to a 'review' state
        # This acts as a trigger for the Client to 'Release Funds'
        job.status = 'completed_by_worker' 
        job.save()
        NotificationService.send(
            recipient=job.client,
            title="Work Completed!",
            message=f"{worker.username} has finished '{job.title}'. Please review and release funds.",
            link=f"/jobs/{job.id}/"
        )
        
        return job