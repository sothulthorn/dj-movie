from movielist_app.models import WatchList, StreamPlateform
from movielist_app.api.serializers import WatchListSerializer, StreamPlateformSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class WatchListAV(APIView):
  
  def get(self, request):
    movies = WatchList.objects.all()
    serializer = WatchListSerializer(movies, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = WatchListSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class WatchDetailsAV(APIView):
  
  def get(self, request, pk):
    if request.method == 'GET':
      try:
        movie = WatchList.objects.get(pk=pk)
      except WatchList.DoesNotExist:
        return Response({'Error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
      
      serializer = WatchListSerializer(movie)
      return Response(serializer.data)
  
  def put(self, request, pk):
    movie = WatchList.objects.get(pk=pk)
    serializer = WatchListSerializer(movie, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def delete(self, request, pk):
    movie = WatchList.objects.get(pk=pk)
    movie.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
  
class StreamPlateformAV(APIView):
  def get(self, request):
    plateform = StreamPlateform.objects.all()
    serializer = StreamPlateformSerializer(plateform, many=True)
    return Response(serializer.data)
  
  def post(self, request):
    serializer = StreamPlateformSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StreamPlateformDetailsAV(APIView):
  def get(self, request, pk):
    if request.method == 'GET':
      try:
        plateform = StreamPlateform.objects.get(pk=pk)
      except StreamPlateform.DoesNotExist:
        return Response({'Error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
      
      serializer = StreamPlateformSerializer(plateform)
      return Response(serializer.data)
  
  def put(self, request, pk):
    plateform = StreamPlateform.objects.get(pk=pk)
    serializer = StreamPlateformSerializer(plateform, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def delete(self, request, pk):
    plateform = StreamPlateform.objects.get(pk=pk)
    plateform.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
