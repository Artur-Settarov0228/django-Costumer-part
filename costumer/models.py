from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name

class CartItem(models.Model):
    name = models.ForeignKey(User , on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def totol_price(self):
        return self.product.price * self.quantity
    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
    
    def __str__(self):
        return f"Buyurtma #{self.id} - {self.user.username}"


