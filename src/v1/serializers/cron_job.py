from django_q.models import Schedule
from rest_framework.serializers import ModelSerializer


class CronJobSerializer(ModelSerializer):
    class Meta:
        model = Schedule
        fields = (
            "pk",
            "name",
            "func",
            "hook",
            "args",
            "kwargs",
            "schedule_type",
            "minutes",
            "repeats",
            "next_run",
            "cron",
            "task",
            "cluster",
            "intended_date_kwarg",
        )
