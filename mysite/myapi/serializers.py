from rest_framework import serializers

from .models import mobile


class mobileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = mobile
        fields = ('id', 'name', 'price')
