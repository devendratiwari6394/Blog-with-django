from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom User Model
    Extends Django's AbstractUser

    AbstractUser already provides:
    - username
    - password (hashed)
    - first_name
    - last_name
    - email
    - is_staff
    - is_superuser
    - date_joined
    """

    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.get_full_name() or self.username