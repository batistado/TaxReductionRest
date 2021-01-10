from taxreductionapp.serializers.formulas import FormulaSerializer
from taxreductionapp.models.formulas import Formulas


class FormulaParser:
    __instance = None

    def __init__(self) -> None:
        self.formula = FormulaSerializer(
            Formulas.objects(), many=True).data[0]
        FormulaParser.__instance = self

    @staticmethod
    def get_instance():
        if FormulaParser.__instance == None:
            FormulaParser()
        return FormulaParser.__instance

    def get_formula_field_list_by_type(self, field, type):
        return [x[field] for x in self.formula[type]]
