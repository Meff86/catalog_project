from django.shortcuts import render, get_object_or_404
from .models import Brand, Category

def home(request):
    brands = Brand.objects.all()
    return render(request, 'home.html', {'brands': brands})

def category_detail(request, brand_id, category_id):
    brand = get_object_or_404(Brand, pk=brand_id)
    category = get_object_or_404(Category, brand=brand, pk=category_id)
    return render(request, 'category_detail.html', {'category': category})