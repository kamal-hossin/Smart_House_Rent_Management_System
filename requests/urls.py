from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RentRequestViewSet, MyRequestsView, AdvertisementRequestsView

router = DefaultRouter()
router.register(r'requests', RentRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('my-requests/', MyRequestsView.as_view(), name='my-requests'),
    path('advertisements/<int:advertisement_id>/requests/', AdvertisementRequestsView.as_view(), name='advertisement-requests'),
]