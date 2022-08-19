from .models import Favorites, Locker, MeMo
from .serializers import FavoriteSerializer, LockerSerializer, MemoSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

class LockerViewSet(ModelViewSet):
    queryset = Locker.objects.all()
    serializer_class = LockerSerializer

    def retrieve(self, request, pk=None):
        instance = self.get_object()
        return Response(self.serializer_class(instance).data,
                        status=status.HTTP_200_OK)
    
    
class MemoViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = MeMo.objects.all()
    serializer_class = MemoSerializer
    
class FavoriteViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Favorites.objects.all()
    serializer_class = FavoriteSerializer