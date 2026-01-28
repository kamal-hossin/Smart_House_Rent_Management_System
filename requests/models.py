from django.db import models
from django.contrib.auth import get_user_model
from advertisements.models import Advertisement

User = get_user_model()

class RentRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='rent_requests')
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rent_requests')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('advertisement', 'requester')

    def save(self, *args, **kwargs):
        if self.status == 'accepted':
            # Reject all other requests for this advertisement
            RentRequest.objects.filter(advertisement=self.advertisement).exclude(id=self.id).update(status='rejected')
            # Prevent new requests
            self.advertisement.is_active = False
            self.advertisement.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Request by {self.requester.username} for {self.advertisement.title}"
