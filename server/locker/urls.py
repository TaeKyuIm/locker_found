from django.urls import path, re_path
from .views import LockerAPI

urlpatterns = [
    path('lockers/', LockerAPI.as_view())
]

# 33.450701, 126.570667
# latitude, longitude