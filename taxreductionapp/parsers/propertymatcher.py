import math
import heapq

from taxreductionapp.models.properties import Properties
from taxreductionapp.serializers.properties import PropertySerializer
from taxreductionapp.parsers.formula import FormulaParser

FORMULA_PARSER = FormulaParser.get_instance()
PER_PAGE_COUNT = 50
RESULT_COUNT = 7


class PropertyMatch:
    def __init__(self, closeness, property) -> None:
        self.closeness = closeness
        self.property = property

    def __lt__(self, other):
        return self.closeness <= other.closeness


def get_similar_properties(propertyID):
    original_property = PropertySerializer(
        Properties.objects(PropertyID=propertyID), many=True).data[0]

    eq_props = FORMULA_PARSER.get_formula_field_list_by_type('property', 'eq')
    lte_props = FORMULA_PARSER.get_formula_field_list_by_type(
        'property', 'lte')

    # Find all eq properties.
    filter = dict()
    for prop in eq_props:
        filter[prop] = original_property[prop]

    # Filter out parent property ID.
    filter['PropertyID'] = {
        '$ne': propertyID
    }

    total_count = Properties.objects(__raw__=filter).count()
    total_pages = total_count // PER_PAGE_COUNT + 1

    properties = list()
    page = 1
    while page < total_pages + 1:
        offset = (page - 1) * PER_PAGE_COUNT

        for property in PropertySerializer(Properties.objects(
                __raw__=filter).skip(offset).limit(PER_PAGE_COUNT), many=True).data:
            base_val = 0
            closeness = 0
            for lte_prop in lte_props:
                base_val += 1 * \
                    (abs(float(property[lte_prop]) -
                         float(original_property[lte_prop]))) ** 2

            if base_val == 0:
                continue
            closeness = 1.0 / math.sqrt(base_val)

            property["__closeness"] = closeness * 100
            if len(properties) < RESULT_COUNT:
                heapq.heappush(properties, PropertyMatch(closeness, property))
            else:
                heapq.heappushpop(
                    properties, PropertyMatch(closeness, property))

        page += 1

    properties = sorted(properties, key=lambda p: p.closeness, reverse=True)
    return [p.property for p in properties]
