from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdvertisementViewSet, AdminAdvertisementViewSet

router = DefaultRouter()
router.register(r'advertisements', AdvertisementViewSet)

admin_router = DefaultRouter()
admin_router.register(r'advertisements', AdminAdvertisementViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', include(admin_router.urls)),
]