from rest_framework import serializers
from rest_framework.reverse import reverse_lazy
from .models import City


class LocationListSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField()
    country = serializers.ReadOnlyField()
    url = serializers.SerializerMethodField()
    def get_url(self, obj):
        days = 1
        return reverse_lazy("locations-detail", request=self.context['request'], kwargs={'name':obj.name}) + '?days=' + str(days)
    class Meta:
        model = City
        fields = ['url', 'name', 'country']

# class LocationsSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=300)
#     url = serializers.SerializerMethodField()
#
#     def get_url(self, obj):
#         days = 1
#         return reverse_lazy("locations-detail", request=self.context['request'], kwargs={'name':obj['name']}) + '?days=' + str(days)
