from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Welcome to the E-commerce API",
        "endpoints": [
            "/api/users/ - Manage users",
            "/api/products/ - Manage products",
            "/api/token/ - Obtain token",
            "/api/token/refresh/ - Refresh token"
        ]
    })
