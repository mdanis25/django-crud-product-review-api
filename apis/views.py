from django.shortcuts import render
from apis.serializers import ProductSerializer, ProductReviewSerializer 
from ecomerce.models import Product, ProductReview 
from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated 

class ProductViewSet(viewsets.ModelViewSet): 
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer 
     
class ProductReviewViewSet(viewsets.ModelViewSet): 
    queryset = ProductReview.objects.all() 
    serializer_class = ProductReviewSerializer 
    