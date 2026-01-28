from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Advertisement(models.Model):
    CATEGORY_CHOICES = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('room', 'Room'),
        ('office', 'Office'),
        ('shop', 'Shop'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='advertisements')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)  
    favorites = models.ManyToManyField(User, related_name='favorite_advertisements', blank=True)

    def save(self, *args, **kwargs):
        if self.status == 'approved':
            self.is_active = True
        else:
            self.is_active = False
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
