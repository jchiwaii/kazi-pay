from .models import Escrow
from decimal import Decimal

def initiate_escrow(job, worker, amount):
    """
    Called when a client accepts a worker's bid.
    Calculates fees and creates the escrow record.
    """
    fee_percentage = Decimal('0.10')  # Example: 10% Platform Fee
    fee = amount * fee_percentage
    payout = amount - fee
    
    escrow = Escrow.objects.create(
        job=job,
        client=job.client,
        worker=worker,
        total_amount=amount,
        platform_fee=fee,
        worker_payout=payout,
        status='pending' # Changes to 'held' once payment callback is received
    )
    return escrow