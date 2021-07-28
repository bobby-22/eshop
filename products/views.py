from django.shortcuts import render, redirect
from django.conf import settings
from django.views import View
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY 

# Create your views here.
def index(request):
    return render(request, "products/index.html")

def success(request):
    return render(request, "products/success.html")

def cancel(request):
    return render(request, "products/cancel.html")

class CheckoutSession(View):
    def post(self, request):
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price": "price_1JHWT5GipF6CtVMryttURxRC",
                    "quantity": 1
                }
            ],
            mode = "payment",
            success_url = "http://127.0.0.1:8000/success",
            cancel_url = "http://127.0.0.1:8000/cancel"
        )
        return redirect(checkout_session.url, code=303)