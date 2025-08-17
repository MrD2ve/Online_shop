from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'orders'

router = DefaultRouter()
router.register(r'orders', views.OrderViewSet)
router.register(r'order-items', views.OrderItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create/', views.order_create, name='order_create'),
    path('admin/order/<int:order_id>/', views.admin_order_detail,
         name='admin_order_detail'),
    path('admin/order/<int:order_id>/pdf/',
         views.admin_order_pdf,
         name='admin_order_pdf')
]