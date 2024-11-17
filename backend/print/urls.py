from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PrintOrderViewSet, download_file

router = DefaultRouter()
router.register('orders', PrintOrderViewSet, basename='printing_logs')


urlpatterns = [
    path('', include(router.urls)),
    path('download_file/', download_file, name='download_file')
]


