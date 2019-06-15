from rest_framework.routers import DefaultRouter

from provider.api import ProviderViewSet, ServiceAreaViewSet


app_name = 'provider'
router = DefaultRouter()
router.register('providers', ProviderViewSet)
router.register('service_area', ServiceAreaViewSet)
