

from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models.climb import Climb
from crag.serializers import ClimbSerializer
# # Create your views here.
class ClimbsView(APIView):
    """View class for climbs/ for viewing all and creating"""
    def get(self, request):
        climbs = Climb.objects.all()
        serializer = ClimbSerializer(climbs, many=True)
        return Response({'climbs': serializer.data})

    def post(self, request):
        serializer = ClimbSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClimbDetailView(APIView):
    """View class for climbs/:pk for viewing a single climb, updating a single climb, or removing a single climb"""
    def get(self, request, pk):
        climb = get_object_or_404(Climb, pk=pk)
        serializer = ClimbSerializer(climb)
        return Response({'climb': serializer.data})

    def patch(self,request, pk):
        climb = get_object_or_404(Climb, pk=pk)
        serializer = ClimbSerializer(climb, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        climb = get_object_or_404(Climb, pk=pk)
        Climb.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)