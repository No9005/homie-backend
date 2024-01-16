from rest_framework.viewsets import ModelViewSet

from data.models import Business
from v1.serializers import BusinessSerializer


class BusinessViewSet(ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
