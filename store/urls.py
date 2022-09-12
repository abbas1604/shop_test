from django.urls import path

from store import views

urlpatterns = [
    path('products/<id>/', views.product_detail),
]
