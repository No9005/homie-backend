from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class TaxConsultant(models.Model):
    firstname = models.TextField(
        max_length=20,
        null=False,
        blank=False,
        verbose_name=_("Firstname"),
    )
    lastname = models.TextField(
        max_length=20,
        null=False,
        blank=False,
        verbose_name=_("Lastname"),
    )
    street = models.TextField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("Street"),
    )
    house_nr = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=_("House Nr."),
    )
    postal = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=_("Postal"),
    )
    city = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=_("City"),
    )
    phone = PhoneNumberField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name=_("Phone"),
    )
    email = models.TextField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name=_("Email"),
    )

    class Meta:
        verbose_name = _("tax consultant")
        verbose_name_plural = _("tax consultants")

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}"

    def clean(self):
        if TaxConsultant.objects.filter(firstname=self.firstname, lastname=self.lastname).exists():
            raise ValidationError(_("Tax consultant '{self}' does already exist"))
