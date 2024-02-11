from rest_framework import serializers
from ..models.verification import Verification

class VerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verification
        fields = ('__all__')