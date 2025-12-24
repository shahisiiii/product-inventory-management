"""User model with role-based access control."""

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom User model with role and email."""

    ADMIN = "ADMIN"
    CUSTOMER = "CUSTOMER"

    ROLE_CHOICES = [
        (ADMIN, "Admin"),
        (CUSTOMER, "Customer"),
    ]

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=CUSTOMER)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        db_table = "users"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.email} ({self.role})"

    @property
    def is_admin(self):
        """Check if user is admin."""
        return self.role == self.ADMIN

    @property
    def is_customer(self):
        """Check if user is customer."""
        return self.role == self.CUSTOMER
