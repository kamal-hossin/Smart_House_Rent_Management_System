from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
from datetime import datetime, timedelta
from .models import Advertisement
from .serializers import AdvertisementSerializer, AdvertisementCreateSerializer, AdvertisementAdminSerializer

class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'status', 'is_active']

    def get_serializer_class(self):
        if self.action == 'create':
            return AdvertisementCreateSerializer
        elif self.request.user.is_authenticated and self.request.user.role == 'admin':
            return AdvertisementAdminSerializer
        return AdvertisementSerializer

    def get_queryset(self):
        queryset = Advertisement.objects.all()
        if self.action == 'list':
            # Only show approved ads to regular users
            if self.request.user.is_authenticated and self.request.user.role != 'admin':
                queryset = queryset.filter(is_active=True)
        return queryset

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated()]
        return []

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def approve(self, request, pk=None):
        if request.user.role != 'admin':
            return Response({'error': 'Only admins can approve advertisements.'}, status=status.HTTP_403_FORBIDDEN)
        advertisement = self.get_object()
        advertisement.status = 'approved'
        advertisement.save()
        return Response({'message': 'Advertisement approved.'})

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def reject(self, request, pk=None):
        if request.user.role != 'admin':
            return Response({'error': 'Only admins can reject advertisements.'}, status=status.HTTP_403_FORBIDDEN)
        advertisement = self.get_object()
        advertisement.status = 'rejected'
        advertisement.save()
        return Response({'message': 'Advertisement rejected.'})

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def toggle_favorite(self, request, pk=None):
        advertisement = self.get_object()
        user = request.user
        if advertisement.favorites.filter(id=user.id).exists():
            advertisement.favorites.remove(user)
            return Response({'message': 'Removed from favorites.'})
        else:
            advertisement.favorites.add(user)
            return Response({'message': 'Added to favorites.'})

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def my_favorites(self, request):
        favorites = request.user.favorite_advertisements.all()
        serializer = AdvertisementSerializer(favorites, many=True)
        return Response(serializer.data)

class AdminAdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementAdminSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role != 'admin':
            return Advertisement.objects.none()
        return super().get_queryset()

    @action(detail=False, methods=['get'])
    def stats(self, request):
        if request.user.role != 'admin':
            return Response({'error': 'Only admins can view stats.'}, status=status.HTTP_403_FORBIDDEN)

        now = datetime.now()
        current_month = now.month
        current_year = now.year
        last_month = (now - timedelta(days=30)).month
        last_month_year = (now - timedelta(days=30)).year

        total_ads = Advertisement.objects.count()
        ads_this_month = Advertisement.objects.filter(created_at__year=current_year, created_at__month=current_month).count()
        ads_last_month = Advertisement.objects.filter(created_at__year=last_month_year, created_at__month=last_month).count()

        return Response({
            'total_advertisements': total_ads,
            'advertisements_this_month': ads_this_month,
            'advertisements_last_month': ads_last_month,
        })
