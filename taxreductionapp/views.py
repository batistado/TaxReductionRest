from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status

from taxreductionapp.models import Properties
from taxreductionapp.serializers import PropertySerializer


@csrf_exempt
def property_detail(request, pk):
    response = {"data": []}
    try:
        serializer = PropertySerializer(
            Properties.objects(PropertyID=pk), many=True)
        response["data"] = serializer.data
    except Properties.DoesNotExist:
        return JsonResponse(response, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return JsonResponse(response)

    return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST)
