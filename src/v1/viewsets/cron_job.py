from django_q.models import Schedule
from rest_framework.viewsets import ReadOnlyModelViewSet

from v1.serializers import CronJobSerializer


class CronJobViewSet(ReadOnlyModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = CronJobSerializer
