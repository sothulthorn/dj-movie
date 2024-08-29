from django.shortcuts import get_object_or_404
from movielist_app.models import WatchList, StreamPlateform, Review
from movielist_app.api.serializers import WatchListSerializer, StreamPlateformSerializer, ReviewSerializer
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from rest_framework.views import APIView

class ReviewCreate(generics.CreateAPIView):
  serializer_class = ReviewSerializer
  
  def perform_create(self, serializer):
    pk = self.kwargs.get('pk')
    movie = WatchList.objects.get(pk=pk)
    
    serializer.save(movielist=movie)

class ReviewList(generics.ListAPIView):
  serializer_class = ReviewSerializer
  
  def get_queryset(self):
    pk = self.kwargs['pk']
    return Review.objects.filter(movielist=pk)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


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
  

class StreamPlateformVS(viewsets.ViewSet):
  def list(self, request):
    queryset = StreamPlateform.objects.all()
    serializer = StreamPlateformSerializer(queryset, many=True)
    return Response(serializer.data)

  def retrieve(self, request, pk=None):
    queryset = StreamPlateform.objects.all()
    movielist = get_object_or_404(queryset, pk=pk)
    serializer = StreamPlateformSerializer(movielist)
    return Response(serializer.data)

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
