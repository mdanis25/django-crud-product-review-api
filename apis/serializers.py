from rest_framework import serializers 
from ecomerce.models import Product, ProductReview 
 
class ProductReviewSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = ProductReview 
        fields = '__all__' 

class ProductReviewShortSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = ProductReview 
        fields = ['rating', 'review'] 
        
class ProductSerializer(serializers.ModelSerializer):
    reviews = ProductReviewShortSerializer(many=True, read_only = True)
    class Meta: 
        model = Product 
        fields = ['name', 'description', 'price', 'reviews'] 

          
    