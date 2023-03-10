from django.db import models
from django.contrib.auth.models import BaseUserModel, PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserModelManager(BaseUserManager):
    """User model manager to create users"""

    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("Email must be provided")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(self._db)

        return user

    def create_super_user(self, email, name, password):
        user = create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)


class UserProfile(BaseUserModel, PermissionsMixin):
    """Create users for the system"""
    email = models.EmailField(max_length=255, required=True)
    name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserModelManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email
