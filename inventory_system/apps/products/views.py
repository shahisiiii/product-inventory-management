"""Product views with caching."""

from rest_framework import viewsets
from rest_framework.response import Response
from django.core.cache import cache
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsAdminOrReadOnly


class ProductViewSet(viewsets.ModelViewSet):
    """ViewSet for Product CRUD operations with caching."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_list_cache_key(self):
        """Generate cache key for product list."""
        return "product_list"

    def get_detail_cache_key(self, pk):
        """Generate cache key for product detail."""
        return f"product_detail_{pk}"

    def list(self, request, *args, **kwargs):
        """List products with caching."""
        cache_key = self.get_list_cache_key()
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        response = super().list(request, *args, **kwargs)
        cache.set(cache_key, response.data, timeout=300)
        return response

    def retrieve(self, request, *args, **kwargs):
        """Retrieve product with caching."""
        pk = kwargs.get("pk")
        cache_key = self.get_detail_cache_key(pk)
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        response = super().retrieve(request, *args, **kwargs)
        cache.set(cache_key, response.data, timeout=300)
        return response

    def create(self, request, *args, **kwargs):
        """Create product and invalidate cache."""
        response = super().create(request, *args, **kwargs)
        cache.delete(self.get_list_cache_key())
        return response

    def update(self, request, *args, **kwargs):
        """Update product and invalidate cache."""
        response = super().update(request, *args, **kwargs)
        pk = kwargs.get("pk")
        cache.delete(self.get_list_cache_key())
        cache.delete(self.get_detail_cache_key(pk))
        return response

    def partial_update(self, request, *args, **kwargs):
        """Partial update product and invalidate cache."""
        response = super().partial_update(request, *args, **kwargs)
        pk = kwargs.get("pk")
        cache.delete(self.get_list_cache_key())
        cache.delete(self.get_detail_cache_key(pk))
        return response

    def destroy(self, request, *args, **kwargs):
        """Delete product and invalidate cache."""
        pk = kwargs.get("pk")
        response = super().destroy(request, *args, **kwargs)
        cache.delete(self.get_list_cache_key())
        cache.delete(self.get_detail_cache_key(pk))
        return response
