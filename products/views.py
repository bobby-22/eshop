from django.shortcuts import render, redirect
from django.conf import settings
from products.models import CategoryModel, ProductModel
from products.serializers import ProductModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY 

# Create your views here.
class Latest(APIView):
    def get(self, request):
        products = ProductModel.objects.all()
        serializers = ProductModelSerializer(products, many=True)
        return Response(serializers.data)

class Details(APIView):
    def get(self, request, stripe_product_id):
        details = ProductModel.objects.filter(stripe_product_id=stripe_product_id)
        serializers = ProductModelSerializer(details, many=True)
        return Response(serializers.data)

class Category(APIView):
    def get(self, request, category_id):
        products = ProductModel.objects.filter(category=category_id)
        serializers = ProductModelSerializer(products, many=True)
        return Response(serializers.data)

#class ProductsSearch(APIView):

class Profile(APIView):
    def get(self, request):
        products = ProductModel.objects.filter(owner=request.user)
        serializers = ProductModelSerializer(products, many=True)
        return Response(serializers.data)

def success(request):
    return render(request, "products/success.html")

def cancel(request):
    return render(request, "products/cancel.html")

class Donate(APIView):
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
