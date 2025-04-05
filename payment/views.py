

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import PaymentForm
from .models import PaymentInformation
from django.contrib.auth.decorators import login_required

@login_required
def payment_view(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user
            payment.subscription_active = True  # Assuming payment success
            payment.save()

            # Send confirmation email
            send_mail(
                'CUFitness Premium Subscription Confirmation',
                'Thank you for subscribing to CUFitness Premium! Your subscription is now active.',
                'noreply@cufitness.com',
                [request.user.email],
                fail_silently=True,
            )

            messages.success(request, 'Payment successful! Premium features unlocked.')
            return redirect('premium-dashboard')  # Change this to actual dashboard view name
        else:
            messages.error(request, 'There were errors with your payment details.')
    else:
        form = PaymentForm()
    return render(request, 'payment/payment_page.html', {'form': form})
