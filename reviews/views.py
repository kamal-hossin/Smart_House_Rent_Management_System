from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Review
from .serializers import ReviewSerializer

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Review.objects.all()
        advertisement_id = self.request.query_params.get('advertisement_id')
        if advertisement_id:
            queryset = queryset.filter(advertisement_id=advertisement_id)
        return queryset