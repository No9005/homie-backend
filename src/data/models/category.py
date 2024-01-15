from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.TextField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name=_("Name"),
    )
    description = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Description"),
    )

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")
