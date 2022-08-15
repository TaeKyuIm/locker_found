from .models import Locker
from .serializers import LockerSerializer
from rest_framework import viewsets

class LockerViewSet(viewsets.ModelViewSet):
    queryset = Locker.objects.all()
    serializer_class = LockerSerializer