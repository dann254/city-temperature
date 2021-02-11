from rest_framework import viewsets
from rest_framework.response import Response
from api.locations.serializers import LocationsSerializer

class LocationsViewSet(viewsets.ViewSet):
    # queryset = [{'message': "this is the way"}]
    # serializer_classes = {
    #     'default': RestaurantListSerializer,
    #     'list': RestaurantListSerializer,
    #     'retrieve': RestaurantSerializer,
    # }
    # lookup_field = 'message'
    # http_method_names = ['get']

    def list(self, request):
        queryset = [{'message': "this is the way"}]
        serializer = LocationsSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, message=None, days=None):
        queryset ={'message': "this is the way"}
        # user = get_object_or_404(queryset, pk=pk)
        # serializer = UserSerializer(user)
        return Response(queryset)
