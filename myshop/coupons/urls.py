from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'coupons'

router = DefaultRouter()
router.register(r'products', views.CouponViewSet, basename='product')

urlpatterns = [
    path('apply/', views.coupon_apply, name='apply'),

    path("api/", include(router.urls)),
]