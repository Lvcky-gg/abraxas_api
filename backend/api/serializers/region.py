from rest_framework import serializers
from ..models.region import Region

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('__all__')