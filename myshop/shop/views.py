from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from rest_framework import viewsets
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.permissions import IsAuthenticated

def product_list(request, category_slug=None):
    category=None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(
        request,
        'shop/product/list.html',
        {
            'category':category,
            'categories':categories,
            'products':products
        }
    )

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()

    return render(
        request,
        'shop/product/detail.html',
        {
            'product':product,
            'cart_product_form':cart_product_form
        }
    )

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
