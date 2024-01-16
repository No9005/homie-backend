from rest_framework.serializers import ModelSerializer

from data.models import TaxConsultant


class TaxConsultantSerializer(ModelSerializer):
    class Meta:
        model = TaxConsultant
        fields = (
            "pk",
            "firstname",
            "lastname",
            "street",
            "house_nr",
            "postal",
            "city",
            "phone",
            "email",
        )
