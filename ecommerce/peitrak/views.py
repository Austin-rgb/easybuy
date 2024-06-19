
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, View
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Transaction, PendingTransaction, CancelledTransaction, RejectedTransaction 
from .forms import SendForm, ReceiveForm
from .api import Transact, Wallet

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = UserCreationForm()
    return render(request, 'store/register.html', {'form': form})


class TransactionListView(LoginRequiredMixin,ListView):
    paginate_by = 10
    model = Transaction 
    template_name = 'store/product_list.html'
    context_object_name = 'products'

    
class PendingTransactionListView(LoginRequiredMixin,ListView):
    paginate_by = 10
    model = PendingTransaction
    template_name = 'store/product_list.html'
    context_object_name = 'products'

    
class CancelledTransactionListView(LoginRequiredMixin,ListView):
    paginate_by = 10
    model = CancelledTransaction
    template_name = 'store/product_list.html'
    context_object_name = 'products'

    
class RejectedTransactionListView(LoginRequiredMixin,ListView):
    paginate_by = 10
    model = RejectedTransaction
    template_name = 'store/product_list.html'
    context_object_name = 'products'
    def get_queryset(self):
        user = self.request.user
        return RejectedTransaction.objects.filter(source=user) | RejectedTransaction.objects.filter(destination=user)
    
def send(request):
    if request.method == 'POST':
        form = SendForm(request.POST, request.FILES)
        if form.is_valid():
            username = request.user.username
            transact = Transact(username)
            transaction, pin = transact.send(form.destination,form.amount)
            return redirect('product_list')
    else:
        form = SendForm()
    return render(request, 'store/upload_product.html', {'form': form})

def receive(request,transaction_id):
    if request.method == 'POST':
        form = ReceiveForm(request.POST, request.FILES)
        if form.is_valid():
            username = request.user.username
            transact = Transact(username)
            transact.receive(transaction_id,form.pin)
            return redirect('product_list')
    else:
        form = ReceiveForm()
    return render(request, 'store/upload_product.html', {'form': form})

def cancel(request,transaction_id):
    if request.method == 'POST':
        form = ReceiveForm(request.POST, request.FILES)
        if form.is_valid():
            username = request.user.username
            transact = Transact(username)
            transact.cancel(transaction_id)
            return redirect('product_list')
    else:
        form = ReceiveForm()
    return render(request, 'store/upload_product.html', {'form': form})

def reject(request,transaction_id):
    if request.method == 'POST':
        form = ReceiveForm(request.POST, request.FILES)
        if form.is_valid():
            username = request.user.username
            transact = Transact(username)
            transact.reject(transaction_id)
            return redirect('product_list')
    else:
        form = ReceiveForm()
    return render(request, 'store/upload_product.html', {'form': form})
