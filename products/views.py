from django.shortcuts import render, redirect
from django.conf import settings
from django.views import View
from .forms import ProductCreateForm
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

class ProductCreate(View):
    def get(self, request):
        form = ProductCreateForm()
        context = {"form": form}
        return render(request, "products/add_product.html", context)

    def post(self, request):
        form = ProductCreateForm(data=request.POST)
        if form.is_valid():
            product_name = form.cleaned_data.get("name")
            product_description = form.cleaned_data.get("description")
            product_price = form.cleaned_data.get("price")
            product = stripe.Product.create(
                name = product_name,
                description = product_description
            )
            stripe.Price.create(
                product = product.id,
                currency = "CZK",
                unit_amount = product_price * 100
            )
            form.save()
            return redirect("products:index")