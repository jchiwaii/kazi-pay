from django.db import transaction
from .models import PlatformRevenue, SystemAuditLog
from escrow.models import Escrow
from wallet.services import WalletService

class AdminFinanceService:
    @staticmethod
    @transaction.atomic
    def resolve_dispute(escrow_id, winner_role, admin_user):
        """
        Manually decides who gets the money in a dispute.
        winner_role: 'worker' or 'client'
        """
        escrow = Escrow.objects.get(id=escrow_id)
        
        if winner_role == 'worker':
            # Release to worker wallet
            WalletService.add_funds(
                user=escrow.worker,
                amount=escrow.worker_payout,
                tx_type='escrow_payout',
                description=f"Dispute resolved in favor of worker for: {escrow.job.title}"
            )
            escrow.status = 'released'
        else:
            # Refund to client wallet (or M-Pesa)
            WalletService.add_funds(
                user=escrow.client,
                amount=escrow.total_amount,
                tx_type='escrow_refund',
                description=f"Dispute refund for: {escrow.job.title}"
            )
            escrow.status = 'refunded'
        
        escrow.save()
        
        # Log the admin action
        SystemAuditLog.objects.create(
            action_by=admin_user,
            action_type="DISPUTE_RESOLUTION",
            details=f"Escrow {escrow_id} resolved for {winner_role}"
        )

class DisputeService:
    @staticmethod
    @transaction.atomic
    def resolve(escrow_id, decision, admin_user):
        """
        decision: 'TOTAL_REFUND' (Client wins) or 'TOTAL_PAYOUT' (Worker wins)
        """
        escrow = Escrow.objects.select_for_update().get(id=escrow_id)
        
        if escrow.status != 'disputed':
            raise ValueError("Only disputed escrows can be resolved.")

        if decision == 'TOTAL_PAYOUT':
            # Pay the worker their net amount (total - fee)
            WalletService.add_funds(
                user=escrow.worker,
                amount=escrow.worker_payout,
                tx_type='escrow_payout',
                description=f"Dispute resolved (Won): {escrow.job.title}"
            )
            escrow.status = 'released'
            
        elif decision == 'TOTAL_REFUND':
            # Refund the client the full amount they paid
            WalletService.add_funds(
                user=escrow.client,
                amount=escrow.total_amount,
                tx_type='escrow_refund',
                description=f"Dispute resolved (Refunded): {escrow.job.title}"
            )
            escrow.status = 'refunded'

        escrow.save()

        # Log for accountability
        SystemAuditLog.objects.create(
            action_by=admin_user,
            action_type="DISPUTE_RESOLVED",
            details=f"Escrow ID {escrow.id} resolved with decision: {decision}"
        )
        
        return escrow
    
