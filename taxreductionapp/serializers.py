from rest_framework_mongoengine import serializers
from taxreductionapp.models import Properties


class PropertySerializer(serializers.DocumentSerializer):
    class Meta:
        model = Properties
        fields = '__all__'
