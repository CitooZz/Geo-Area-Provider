from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework_gis.filters import InBBoxFilter
from rest_framework_gis.pagination import GeoJsonPagination


from provider.models import Provider, ServiceArea
from provider.serializers import ProviderSerializer, ServiceAreaSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    """
    list:
    Return list of provider.

    create:
    Create provider.
    Parameters :
    - name: "Provider name"
    - email: "provider@provider.com"
    - phone_number: "+199999999999" # Should start with +1
    - language: "English / Indonesian"
    - currency: "USD / IDR"

    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    permission_classes = [permissions.IsAuthenticated]


class ServiceAreaViewSet(viewsets.ModelViewSet):
    """
    list:
    Return list of service area.
    To filter polygon geometry use this paramter ?in_bbox=-90,30,150,50 (min lat, min lng, max lat, max lng)

    create:
    Create service area.
    Parameters :
        - provider: "provider ID",
        - name: "Service Area name",
        - price: 100,
        - geometry: Polygon data

        example :

        {
            "provider": 1,
            "name": "area 2",
            "price": 10,
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [
                            135.0,
                            45.0
                        ],
                        [
                            140.0, 
                            50.0
                        ],
                        [
                            145.0, 
                            55.0
                        ],
                        [
                            135.0, 
                            45.0
                        ]
                    ]
                ]
            }
        }
    """
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
    permission_classes = [permissions.IsAuthenticated]
    bbox_filter_field = 'geometry'
    filter_backends = (InBBoxFilter, )
    bbox_filter_include_overlapping = True
    pagination_class = GeoJsonPagination

    # Cache for 2 hours
    @method_decorator(cache_page(60 * 60 * 2))
    def dispatch(self, *args, **kwargs):
        return super(ServiceAreaViewSet, self).dispatch(*args, **kwargs)
