from rest_framework import serializers
from ..models.publication import Publication

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ('__all__')