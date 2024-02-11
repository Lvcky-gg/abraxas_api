from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from ..serializers.person import PersonSerializer
from ..models.person import Person


@api_view(['GET'])
def people_list(request):
    people = Person.objects.all().order_by('-id')
    serializer = PersonSerializer(people, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def person_detail(request, pk):
    person = Person.objects.get(id=pk)
    serializer = PersonSerializer(person, many=False)
    
    return Response(serializer.data)

@api_view(['POST'])
def person_create(request):
    serializer = PersonSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['PUT'])
def person_edit(request, pk):
    person = Person.objects.get(id=pk)
    serializer = PersonSerializer(instance=person, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def person_delete(request, pk):
    person = Person.objects.get(id=pk)
    person.delete()
    
    return Response('Person was deleted')
