from django.db import models
from django.utils.translation import gettext_lazy as _


class Business(models.Model):
    name = models.TextField(
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("Name"),
    )

    class Meta:
        verbose_name = _("business")
        verbose_name_plural = _("businesses")

    def __str__(self) -> str:
        return f"{self.name}"
