from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import RentRequest
from .serializers import RentRequestSerializer, RentRequestCreateSerializer, RentRequestOwnerSerializer

class RentRequestViewSet(ModelViewSet):
    queryset = RentRequest.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return RentRequestCreateSerializer
        elif self.request.user.role == 'admin' or any(self.request.user == req.advertisement.owner for req in self.get_queryset()):
            return RentRequestOwnerSerializer
        return RentRequestSerializer

    def get_queryset(self):
        queryset = RentRequest.objects.all()
        if self.request.user.role != 'admin':
            # Users can see their own requests or requests for their ads
            queryset = queryset.filter(
                requester=self.request.user
            ) | queryset.filter(
                advertisement__owner=self.request.user
            )
        return queryset.distinct()

class MyRequestsView(generics.ListAPIView):
    serializer_class = RentRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return RentRequest.objects.filter(requester=self.request.user)

class AdvertisementRequestsView(generics.ListAPIView):
    serializer_class = RentRequestOwnerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        advertisement_id = self.kwargs['advertisement_id']
        return RentRequest.objects.filter(
            advertisement_id=advertisement_id,
            advertisement__owner=self.request.user
        )