from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status

from taxreductionapp.models.properties import Properties
from taxreductionapp.serializers.properties import PropertySerializer, PropertyAddressSerializer
from taxreductionapp.middleware.cache import AutoComplete
from taxreductionapp.parsers.formula import FormulaParser

FORMULA_PARSER = FormulaParser.get_instance()
ADDRESS_LIMIT = 5
CACHE = AutoComplete.get_instance()


def get_similar_properties(propertyID):
    original_property = PropertySerializer(
        Properties.objects(PropertyID=propertyID), many=True).data[0]

    eq_props = FORMULA_PARSER.get_formula_field_list_by_type('property', 'eq')
    lte_props = FORMULA_PARSER.get_formula_field_list_by_type(
        'property', 'lte')

    filter = dict()
    for prop in eq_props:
        filter[prop] = original_property[prop]

    return PropertySerializer(
        Properties.objects(__raw__=filter), many=True).data


@csrf_exempt
def similar_properties_by_id(request, propertyID):
    response = {"data": []}
    try:
        response["data"] = get_similar_properties(propertyID)
    except Properties.DoesNotExist:
        return JsonResponse(response, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return JsonResponse(response)

    return JsonResponse(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
def property_by_id(request, propertyID):
    response = {"data": []}
    try:
        serializer = PropertySerializer(
            Properties.objects(PropertyID=propertyID), many=True)
        response["data"] = serializer.data
    except Properties.DoesNotExist:
        return JsonResponse(response, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return JsonResponse(response)

    return JsonResponse(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
def property_by_address(request):
    response = {"data": []}
    try:
        address = request.GET['address']

        response["data"] = CACHE.get(address)
        if not response["data"]:
            serializer = PropertyAddressSerializer(
                Properties.objects(Situs__istartswith=address)[:ADDRESS_LIMIT], many=True)

            CACHE.add(address, serializer.data)
            response["data"] = serializer.data

    except Properties.DoesNotExist:
        return JsonResponse(response, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print(e)
        return JsonResponse(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if request.method == 'GET':
        return JsonResponse(response)

    return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST)
