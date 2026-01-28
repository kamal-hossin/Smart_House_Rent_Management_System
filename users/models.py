from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    email_verification_token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    is_email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username
