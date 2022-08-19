from .models import Locker, MeMo
from rest_framework import serializers

class LockerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locker
        fields = '__all__'
        

class MemoSerializer(serializers.ModelSerializer):
    locker = LockerSerializer(many=True, read_only=True)
    class Meta:
        model = MeMo
        fields = '__all__'
        
        
class FavoriteSerializer(serializers.ModelSerializer):
    locker = LockerSerializer(many=True, read_only=True)
    class Meta:
        model = MeMo
        fields = '__all__'