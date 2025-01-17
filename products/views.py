from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.http import JsonResponse
from django.db.models import Q

def search_products(request):
    query = request.GET.get('q', '')  # Get the search query from request parameters
    if query:
        # Filter products by name or category
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(category__icontains=query)
        )
    else:
        # If no query is provided, return an empty list
        products = Product.objects.none()

    # Serialize the products
    product_list = [{"name": product.name, "description": product.description, "price": product.price, "category": product.category} for product in products]
    
    return JsonResponse({"products": product_list})



# View for listing products (GET) and creating a product (POST)
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# View for creating a new product (POST)
class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create a product

# View for retrieving, updating, or deleting a product (GET, PUT, DELETE)
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
