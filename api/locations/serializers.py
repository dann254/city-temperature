from rest_framework import serializers
from rest_framework.reverse import reverse_lazy

class LocationsSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=300)
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        return reverse_lazy("locations-detail", request=self.context['request'], kwargs={'message':obj['message'], 'days':1})
