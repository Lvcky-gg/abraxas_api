from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from ..serializers.quote import QuoteSerializer
from ..models.quote import Quote

@api_view(['GET'])
def quotes_list(request):
    quotes = Quote.objects.all().order_by('-id')
    serializer = QuoteSerializer(quotes, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def quote_detail(request, pk):
    quote = Quote.objects.get(id=pk)
    serializer = QuoteSerializer(quote, many=False)
    
    return Response(serializer.data)

@api_view(['POST'])
def quote_create(request):
    serializer = QuoteSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['PUT'])
def quote_edit(request, pk):
    quote = Quote.objects.get(id=pk)
    serializer = QuoteSerializer(instance=quote, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def quote_delete(request, pk):
    quote = Quote.objects.get(id=pk)
    quote.delete()
    
    return Response('Quote was deleted')

