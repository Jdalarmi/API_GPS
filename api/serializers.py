from rest_framework import serializers

from api.models import Address, Position


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['name', 'x', 'y']
        
class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'