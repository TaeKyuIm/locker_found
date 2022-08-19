from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = "locker"

router = DefaultRouter()
router.register(r'lockers', views.LockerViewSet)
router.register(r'memo', views.MemoViewSet)

urlpatterns = router.urls

# from rest_framework import routers
# from .views import LockerViewSet

# router = routers.SimpleRouter()
# router.register('lockers', LockerViewSet)

# urlpatterns = router.urls