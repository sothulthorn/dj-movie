from rest_framework import serializers
from movielist_app.models import WatchList, StreamPlateform, Review

class ReviewSerializer(serializers.ModelSerializer):
  review_user = serializers.StringRelatedField(read_only=True)
  
  class Meta:
    model = Review
    # fields = "__all__"
    exclude = ('movielist',)

class WatchListSerializer(serializers.ModelSerializer):
  reviews = ReviewSerializer(many=True, read_only=True)
  
  class Meta:
    model = WatchList
    fields = "__all__"

class StreamPlateformSerializer(serializers.ModelSerializer):
  movielist = WatchListSerializer(many=True, read_only=True)
  
  class Meta:
    model = StreamPlateform
    fields = "__all__"
    
