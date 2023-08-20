from django.shortcuts import render, redirect
from .models import Payment
from .forms import CreatePaymentForm


def create_payment_form(request):
    form = CreatePaymentForm()
    return render(request, 'payments/create_payment.html', {'form': form})


def create_payment(request):
    if request.method == 'POST':
        amount = request.PoST['amount']
        description = request.POST['description']
        Payment.object.create(amount=amount, description=description)
        return redirect('payment_list')
    return render(request, 'create_payment.html')


def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payment_list.html', {'payments': payments})