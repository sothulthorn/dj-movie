from django.urls import path, include
from movielist_app.api.views import WatchListAV, WatchDetailsAV, StreamPlateformAV, StreamPlateformDetailsAV

urlpatterns = [
    path("list/", WatchListAV.as_view(), name="movie-list"),
    path("<int:pk>", WatchDetailsAV.as_view(), name='movie-details'),
    path("stream/", StreamPlateformAV.as_view(), name="stream-list"),
    path("stream/<int:pk>", StreamPlateformDetailsAV.as_view(), name="stream-details")
]