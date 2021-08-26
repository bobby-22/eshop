from django.shortcuts import(
    render,
    redirect
) 
from django.conf import settings
from products.models import ProductModel
from products.serializers import ProductModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import(
    generics,
    filters
)
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY 

# Create your views here.
class LatestView(APIView):
    def get(self, request):
        queryset = ProductModel.objects.all()
        serializers = ProductModelSerializer(queryset, many=True, context={"request": request})
        return Response(serializers.data)

class DetailsView(APIView):
    def get(self, request, stripe_product_id):
        details = ProductModel.objects.filter(stripe_product_id=stripe_product_id)
        serializers = ProductModelSerializer(details, many=True, context={"request": request})
        return Response(serializers.data)

class CategoryView(APIView):
    def get(self, request, category_id):
        queryset = ProductModel.objects.filter(category=category_id)
        serializers = ProductModelSerializer(queryset, many=True, context={"request": request})
        return Response(serializers.data)

class SearchView(generics.ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "description", "location"]

class ProfileView(APIView):
    def get(self, request):
        queryset = ProductModel.objects.filter(owner=request.user)
        serializers = ProductModelSerializer(queryset, many=True, context={"request": request})
        return Response(serializers.data)

def success(request):
    return render(request, "products/success.html")

def cancel(request):
    return render(request, "products/cancel.html")

class DonateView(APIView):
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
