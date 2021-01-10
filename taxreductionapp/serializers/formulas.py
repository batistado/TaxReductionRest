from rest_framework_mongoengine import serializers
from taxreductionapp.models.formulas import Formulas


class FormulaSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Formulas
        fields = '__all__'
