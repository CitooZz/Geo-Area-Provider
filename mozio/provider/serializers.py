from rest_framework import serializers
from rest_framework_gis import serializers as gis_serializers

from provider.models import Provider, ServiceArea


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = ('id', 'name', 'email', 'phone_number', 'language', 'currency')


class ServiceAreaSerializer(gis_serializers.GeoFeatureModelSerializer):

    class Meta:
        model = ServiceArea
        geo_field = "geometry"
        fields = ('id', 'provider', 'name', 'price', 'geometry')
