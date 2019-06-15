from django.db import models
from django.core.validators import RegexValidator
from django.contrib.gis.db import models as gismodels

from provider.constants import Language, Currency


class Provider(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=17, validators=[phone_regex])

    language = models.CharField(max_length=20, choices=Language.choices)
    currency = models.CharField(max_length=20, choices=Currency.choices)

    class Meta:
        unique_together = ('email', 'phone_number')

    def __str__(self):
        return self.name


class ServiceArea(models.Model):
    provider = models.ForeignKey(Provider, related_name='service_areas', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0)

    geometry = gismodels.PolygonField()

    def __str__(self):
        return '{} {}'.format(self.provider, self.name)
