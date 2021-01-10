from rest_framework_mongoengine import serializers
from taxreductionapp.models.models import Properties


class PropertySerializer(serializers.DocumentSerializer):
    class Meta:
        model = Properties
        fields = '__all__'


class PropertyAddressSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Properties
        fields = ('PropertyID', 'Situs')
