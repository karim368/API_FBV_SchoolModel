from django.shortcuts import render

# Create your views here.
from app.models import *
from rest_framework.response import Response
from app.serializers import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['get','post'])
@permission_classes([IsAuthenticated])
def SDJ(request):
    sdo = School.objects.all()
    jsonobj = SchoolModelSerializer(sdo,many = True)
    jsondata = jsonobj.data
    return Response(jsondata)