"""Product serializers."""

from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product model."""

    class Meta:
        model = Product
        fields = ["id", "name", "price", "stock", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_price(self, value):
        """Validate price is not negative."""
        if value < 0:
            raise serializers.ValidationError("Price cannot be negative.")
        return value

    def validate_stock(self, value):
        """Validate stock is not negative."""
        if value < 0:
            raise serializers.ValidationError("Stock cannot be negative.")
        return value

    def validate_name(self, value):
        """Validate name is not empty."""
        if not value or not value.strip():
            raise serializers.ValidationError("Name is required.")
        return value.strip()
