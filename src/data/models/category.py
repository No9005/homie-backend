from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.TextField(
        max_length=50,
        null=False,
        blank=False,
        unique=True,
        verbose_name=_("Name"),
    )
    description = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Description"),
    )

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self) -> str:
        return f"{self.name}"
