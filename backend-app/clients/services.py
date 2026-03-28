from django.db import transaction
from rest_framework.exceptions import ValidationError
from escrow.services import initiate_escrow  # Import from our escrow app

class JobService:
    @staticmethod
    @transaction.atomic
    def accept_worker_bid(job, bid):
        """
        Logic to accept a bid, close the job to other bidders,
        and trigger the escrow process.
        """
        if job.status != 'open':
            raise ValidationError("This job is no longer accepting bids.")
        
        # 1. Update Job
        job.status = 'in_progress'
        job.assigned_worker = bid.worker
        job.save()
        
        # 2. Mark this bid as accepted
        bid.is_accepted = True
        bid.save()
        
        # 3. Trigger Escrow (Status will be 'pending' until paid)
        escrow_record = initiate_escrow(
            job=job, 
            worker=bid.worker, 
            amount=bid.amount
        )
        
        return job, escrow_record