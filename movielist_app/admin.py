from django.contrib import admin
from movielist_app.models import WatchList, StreamPlateform, Review

# Register your models here.
admin.site.register(WatchList)
admin.site.register(StreamPlateform)
admin.site.register(Review)