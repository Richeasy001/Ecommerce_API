from django.db import models
from users.models import CustomUser

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    stock_quantity = models.PositiveIntegerField()
    image_url = models.URLField(max_length=1024, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="products", null=False)

    def __str__(self):
        return self.name

    def reduce_stock(self, quantity):
        if self.stock_quantity >= quantity:
            self.stock_quantity -= quantity
            self.save()
        else:
            raise ValueError("Not enough stock available.")

