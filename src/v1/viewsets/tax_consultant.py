from rest_framework.viewsets import ModelViewSet

from data.models import TaxConsultant
from v1.serializers import TaxConsultantSerializer


class TaxConsultantViewSet(ModelViewSet):
    queryset = TaxConsultant.objects.all()
    serializer_class = TaxConsultantSerializer
