from rest_framework import serializers
from ..models.quote import Quote

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ('__all__')