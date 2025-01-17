from django.urls import path
from .views import ProductListView, ProductCreateView, ProductDetailView, search_products

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),  # GET list of products
    path('create/', ProductCreateView.as_view(), name='product-create'),  # POST create a product
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),  # GET, PUT, DELETE product details
    path('search/', search_products, name='search_products'),
]
