from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet

app_name = 'shop'

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('', views.product_list, name='product_list'),

    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path("api/", include(router.urls)),
    path(
        '<slug:category_slug>/',
        views.product_list,
        name='product_list_by_category'
    ),

]