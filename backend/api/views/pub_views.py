from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from ..serializers.publication import PublicationSerializer
from ..models.publication import Publication



@api_view(['GET'])
def pubs_list(request):
    pubs = Publication.objects.all().order_by('-id')
    serializer = PublicationSerializer(pubs, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def pub_detail(request, pk):
    pub = Publication.objects.get(id=pk)
    serializer = PublicationSerializer(pub, many=False)
    
    return Response(serializer.data)

@api_view(['POST'])
def pub_create(request):
    serializer = PublicationSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)
@api_view(['PUT'])
def pub_edit(request, pk):
    pub = Publication.objects.get(id=pk)
    serializer = PublicationSerializer(instance=pub, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)
@api_view(['DELETE'])
def pub_delete(request, pk):
    pub = Publication.objects.get(id=pk)
    pub.delete()
    
    return Response('Publication was deleted')

