"""Product model."""

from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    """Product model with validation."""

    name = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "products"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - ${self.price}"
