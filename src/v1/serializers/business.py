from rest_framework.serializers import ModelSerializer

from data.models import Business


class BusinessSerializer(ModelSerializer):
    class Meta:
        model = Business
        fields = (
            "pk",
            "name",
        )
