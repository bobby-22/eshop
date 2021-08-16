from django.shortcuts import render, redirect
from django.conf import settings
from products.models import ProductModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import ProductForm
from django.http import JsonResponse
from rest_framework.views import APIView
from products.serializers import ProductModelSerializer
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY 

# Create your views here.
def success(request):
    return render(request, "products/success.html")

def cancel(request):
    return render(request, "products/cancel.html")

class Donate(View):
    def post(self, request):
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price": "price_1JNJftGipF6CtVMryAn0ON5T",
                    "quantity": 1
                },
                {
                    "price": "price_1JNJftGipF6CtVMrlCfxytYD",
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
    serializers = ProductModelSerializer(products, many=True)
    return JsonResponse(serializers.data, safe=False)

def latest(self):
    products = ProductModel.objects.all()
    serializers = ProductModelSerializer(products, many=True)
    return JsonResponse(serializers.data, safe=False)

class ProductCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = ProductForm()
        context = {"form": form}
        return render(request, "products/product_create.html", context)

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
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

class ProductDetails(APIView):
    def get(self, request, stripe_product_id):
        details = ProductModel.objects.all().filter(stripe_product_id=stripe_product_id)
        serializers = ProductModelSerializer(details, many=True)
        return JsonResponse(serializers.data, safe=False)

    def put(self, request, stripe_product_id):
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

    def delete(self, request, stripe_product_id):
        product = ProductModel.objects.get(stripe_product_id=stripe_product_id)
        if product.owner != request.user:
            return redirect("products:product_read")
        stripe.Product.modify(
            stripe_product_id,
            active = "false"
        )
        product.delete()
