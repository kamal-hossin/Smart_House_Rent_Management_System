#!/usr/bin/env python
import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'house_rent.settings')
django.setup()

from users.models import User

# Create admin user
if not User.objects.filter(username='admin').exists():
    user = User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='admin123'
    )
    user.role = 'admin'
    user.is_email_verified = True
    user.is_active = True
    user.save()
    print("Admin user created.")
else:
    print("Admin user already exists.")