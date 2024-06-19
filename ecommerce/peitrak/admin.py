from django.contrib import admin
from  .models import Account, PendingTransaction, Transaction, CancelledTransaction, RejectedTransaction
# Register your models here.
admin.register(Account)
admin.register(PendingTransaction)
admin.register(Transaction)
admin.register(CancelledTransaction)
admin.register(RejectedTransaction)