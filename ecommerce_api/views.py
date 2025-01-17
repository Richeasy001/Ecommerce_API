from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Welcome to the E-commerce API",
        "endpoints": [
            "/api/users/ - Manage users",
            "/api/users/register/ - Create new user",
            "/api/users/login/ - Login to user account(Get JWT access and refresh token)",
            "/api/products/ - List products",
            "/api/products/create/ - Create new product(for authenticated users)",
            "/api/products/<int>/ - Perform CRUD operations on the products",
            "/api/token/ - Obtain token",
            "/api/token/refresh/ - Refresh token",
        ]
    })
