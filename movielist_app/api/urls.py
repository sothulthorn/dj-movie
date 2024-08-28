from django.urls import path, include
# from movielist_app.api.views import movie_list, movie_details
from movielist_app.api.views import MovieListAV, MovieDetailsAV

urlpatterns = [
    path("list/", MovieListAV.as_view(), name="movie-list"),
    path("<int:pk>", MovieDetailsAV.as_view(), name='movie-details')
]