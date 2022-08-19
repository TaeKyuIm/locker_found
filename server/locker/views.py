from .models import Locker, MeMo
from .serializers import LockerSerializer, MemoSerializer
from rest_framework.viewsets import ModelViewSet

class LockerViewSet(ModelViewSet):
    queryset = Locker.objects.all()
    serializer_class = LockerSerializer
    
    
class MemoViewSet(ModelViewSet):
    queryset = MeMo.objects.all()
    serializer_class = MemoSerializer