from products.models import ProductModel
from django.shortcuts import render, redirect
from django.conf import settings
from django.views import View
from .forms import ProductForm
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
        form = ProductForm()
        context = {"form": form}
        return render(request, "products/product_create.html", context)

    def post(self, request):
        form = ProductForm(data=request.POST)
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
            model_instance = form.save(commit=False)
            model_instance.product_id_stripe = product.id
            model_instance.save()
            return redirect("products:index")
        context = {"form": form}
        return render(request, "products/product_create.html", context)

def product_read(request):
    products = ProductModel.objects.all()

    context = {"products": products}
    return render(request, "products/product_read.html", context)

def product_details(request, product_id):
    product = ProductModel.objects.get(id=product_id)

    context = {"product": product}
    return render(request, "products/product_details.html", context)
