from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    # Add or customize fields here if needed
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",  # Avoids conflict with the default User model
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_set",  # Avoids conflict with the default User model
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
