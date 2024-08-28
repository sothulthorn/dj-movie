from rest_framework import serializers
from movielist_app.models import WatchList, StreamPlateform

class WatchListSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = WatchList
    fields = "__all__"

class StreamPlateformSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = StreamPlateform
    fields = "__all__"