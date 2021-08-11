from django.contrib.auth import login
from products.models import ProductModel
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import ProductForm
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY 

# Create your views here.
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

def index(request):
    return render(request, "products/index.html")

def cables(request):
    products = ProductModel.objects.all().filter(category=1)
    context = {"products": products}
    return render(request, "products/cables.html", context)

def deskmats(request):
    products = ProductModel.objects.all().filter(category=2)
    context = {"products": products}
    return render(request, "products/deskmats.html", context)

def keyboards(request):
    products = ProductModel.objects.all().filter(category=3)
    context = {"products": products}
    return render(request, "products/keyboards.html", context)

def keycaps(request):
    products = ProductModel.objects.all().filter(category=4)
    context = {"products": products}
    return render(request, "products/keycaps.html", context)

def switches(request):
    products = ProductModel.objects.all().filter(category=5)
    context = {"products": products}
    return render(request, "products/switches.html", context)

def others(request):
    products = ProductModel.objects.all().filter(category=6)
    context = {"products": products}
    return render(request, "products/others.html", context)

@login_required
def profile(request):
    products = ProductModel.objects.all().filter(owner=request.user)
    context = {"products": products}
    return render(request, "products/profile.html", context)

class ProductCreate(LoginRequiredMixin, View):
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
            price = stripe.Price.create(
                product = product.id,
                currency = "CZK",
                unit_amount = product_price * 100
            )
            model_instance = form.save(commit=False)
            model_instance.owner = request.user
            model_instance.stripe_product_id = product.id
            model_instance.stripe_price_id = price.id
            model_instance.save()
            return redirect("products:index")

def product_read(request):
    products = ProductModel.objects.all()
    context = {"products": products}
    return render(request, "products/product_read.html", context)

def product_details(request, stripe_product_id):
    objects = ProductModel.objects.all().filter(stripe_product_id=stripe_product_id)
    for object in objects:
        date_added = object.date_added
        name = object.name
        description = object.description
        price = object.price
        owner = object.owner
        category = object.category

    context = {"date_added": date_added, "name": name, "description": description, "price": price, "owner": owner, "category": category}
    return render(request, "products/product_details.html", context)

class ProductUpdate(LoginRequiredMixin, View):
    def get(self, request, stripe_product_id):
        product = ProductModel.objects.get(stripe_product_id=stripe_product_id)
        if product.owner != request.user:
            return redirect("products:product_read")
        form = ProductForm(instance=product)
        context = {"product": product, "form": form}
        return render(request, "products/product_update.html", context)

    def post(self, request, stripe_product_id):
        product = ProductModel.objects.get(stripe_product_id=stripe_product_id)
        form = ProductForm(instance=product, data=request.POST)
        if form.is_valid():
            product_name = form.cleaned_data.get("name")
            product_description = form.cleaned_data.get("description")
            product_price = form.cleaned_data.get("price")
            if "price" in form.changed_data:
                stripe.Price.modify(
                    product.stripe_price_id,
                    active = "false"
                )
                price = stripe.Price.create(
                    product = stripe_product_id,
                    currency = "CZK",
                    unit_amount = product_price * 100
                )
                product.stripe_price_id = price.id
            if "name" in form.changed_data:
                stripe.Product.modify(
                    stripe_product_id,
                    name = product_name,
                    )
            if "description" in form.changed_data:
                stripe.Product.modify(
                    stripe_product_id,
                    description = product_description
                )
            form.save()
            return redirect("products:index")

@login_required
def product_delete(request, stripe_product_id):
    if request.method == "GET":
        product = ProductModel.objects.get(stripe_product_id=stripe_product_id)
        if product.owner != request.user:
            return redirect("products:product_read")
        stripe.Product.modify(
            stripe_product_id,
            active = "false"
        )
        product.delete()
        return redirect("products:product_read")

    return render(request, "products/product_read.html")
