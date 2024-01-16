from rest_framework.serializers import ModelSerializer

from data.models import TaxConsultant


class TaxConsultantSerializer(ModelSerializer):
    class Meta:
        model = TaxConsultant
        fields = "__all__"
