from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER = 'user'
    ADMIN = 'admin'

    ROLE_CHOICES = [
        (USER, 'User'),
        (ADMIN, 'Admin'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=USER)

    def is_admin(self):
        return self.role == self.ADMIN
