from django.contrib import admin
from django.urls import path

from .views import send, receive
from .views import TransactionListView

urlpatterns = [
    path('transactions/', TransactionListView.as_view(), name='transaction-list'),
    path('send/',send,name='send'),
    path('receive/<str:transaction_id>',receive,name='receive')
    ]
