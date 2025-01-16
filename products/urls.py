from django.urls import path
from .views import ProductListView, ProductCreateView, ProductDetailView

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),  # GET list of products
    path('create/', ProductCreateView.as_view(), name='product-create'),  # POST create a product
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),  # GET, PUT, DELETE product details
]
