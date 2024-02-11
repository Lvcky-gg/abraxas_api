from ..models.person import Person
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    # added_by = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Person
        fields = '__all__'

    # def get_added_by(self, obj):
    #     added_by = obj.added_by
    #     serializer = UserSerializer(added_by, many=False)
    #     return serializer.data