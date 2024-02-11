from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from ..serializers.verification import VerificationSerializer
from ..models.verification import Verification

@api_view(['GET'])
def verifications_list(request):
    verifications = Verification.objects.all().order_by('-id')
    serializer = VerificationSerializer(verifications, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def verification_detail(request, pk):
    verification = Verification.objects.get(id=pk)
    serializer = VerificationSerializer(verification, many=False)
    
    return Response(serializer.data)

@api_view(['POST'])
def verification_create(request):
    serializer = VerificationSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['PUT'])
def verification_edit(request, pk):
    verification = Verification.objects.get(id=pk)
    serializer = VerificationSerializer(instance=verification, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def verification_delete(request, pk):
    verification = Verification.objects.get(id=pk)
    verification.delete()
    
    return Response('Verification was deleted')
