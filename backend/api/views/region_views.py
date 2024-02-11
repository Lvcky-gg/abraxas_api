from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from ..serializers.region import RegionSerializer
from ..models.region import Region

@api_view(['GET'])
def regions_list(request):
    regions = Region.objects.all().order_by('-id')
    serializer = RegionSerializer(regions, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def region_detail(request, pk):
    region = Region.objects.get(id=pk)
    serializer = RegionSerializer(region, many=False)
    
    return Response(serializer.data)

@api_view(['POST'])
def region_create(request):
    serializer = RegionSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['PUT'])
def region_edit(request, pk):
    region = Region.objects.get(id=pk)
    serializer = RegionSerializer(instance=region, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def region_delete(request, pk):
    region = Region.objects.get(id=pk)
    region.delete()
    
    return Response('Region was deleted')
