from django.contrib import admin
from ecomerce.models import Product, ProductReview

@admin.register(Product) 
class ProductAdmin(admin.ModelAdmin): 
    list_display = ['name', 'description', 'price']
 
 
@admin.register(ProductReview) 
class ProductReviewAdmin(admin.ModelAdmin): 
    list_display = ['product', 'user', 'rating', 'review', 'created_at', 'updated_at']
    
     