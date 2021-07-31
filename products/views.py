import products
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
            model_instance = form.save()
            product = stripe.Product.create(
                name = model_instance.name,
                description = model_instance.description
            )
            price = stripe.Price.create(
                product = product.id,
                currency = "CZK",
                unit_amount = model_instance.price * 100
            )
            model_instance.stripe_product_id = product.id
            model_instance.stripe_price_id = price.id
            model_instance.save()
            return redirect("products:index")
        context = {"form": form}
        return render(request, "products/product_create.html", context)

def product_read(request):
    products = ProductModel.objects.all()

    context = {"products": products}
    return render(request, "products/product_read.html", context)

def product_details(request, stripe_product_id):
    objects = ProductModel.objects.all().filter(stripe_product_id=stripe_product_id)
    for object in objects:
        name = object.name
        description = object.description
        price = object.price

    context = {"name": name, "description": description, "price": price}
    return render(request, "products/product_details.html", context)

class ProductUpdate(View):
    def get(self, request, stripe_product_id):
        product = ProductModel.objects.get(stripe_product_id=stripe_product_id)
        objects = ProductModel.objects.filter(stripe_product_id=stripe_product_id)
        for object in objects:
            placeholder = object
        form = ProductForm(instance=object)
        context = {"product": product, "form": form}
        return render(request, "products/product_update.html", context)

    def post(self, request, stripe_product_id):
        objects = ProductModel.objects.filter(stripe_product_id=stripe_product_id)
        for object in objects:
            placeholder = object
        form = ProductForm(instance=object, data=request.POST)
        if form.is_valid():
            stripe.Price.modify(
                ProductModel.objects.get(stripe_product_id=stripe_product_id).stripe_price_id,
                active = "false"
            )
            model_instance = form.save()
            stripe.Product.modify(
                stripe_product_id,
                name = model_instance.name,
                description = model_instance.description
                )
            price = stripe.Price.create(
                product = stripe_product_id,
                currency = "CZK",
                unit_amount = model_instance.price * 100
            )
            model_instance.stripe_price_id = price.id
            model_instance.save()
            return redirect("products:index")
        context = {"form": form}
        return render(request, "products/product_update.html", context)
