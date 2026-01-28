from django.db import models
from django.contrib.auth import get_user_model
from advertisements.models import Advertisement

User = get_user_model()

class Review(models.Model):
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])  # 1 to 5
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('advertisement', 'reviewer')

    def __str__(self):
        return f"Review by {self.reviewer.username} for {self.advertisement.title}"
