from rest_framework import routers
from .views import LockerViewSet

router = routers.SimpleRouter()
router.register('lockers', LockerViewSet)

urlpatterns = router.urls