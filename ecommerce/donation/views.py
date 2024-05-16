from django.shortcuts import render
import stripe
from django.urls import reverse

from ecommerce import settings


def my_donation(request):
    stripe.api_key = settings.STRIPE_PRIVATE_KEY
    session = stripe.checkout.Session.create(
        line_items=[{
            'price': 'price_1PHAy5EShB3ZT1fJIuQzgYEN',
            'quantity': 1
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('payment-success')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('payment-failed')),
    )
    return render(request, 'donation/my-donation.html',
                  {'session_id': session.id,
                    'stripe_public_key': settings.STRIPE_PUBLIC_KEY})


def payment_success(request):
    return render(request, 'donation/payment-success.html')


def payment_failed(request):
    return render(request, 'donation/payment-failed.html')