from django.urls import path, include
from rest_framework.routers import DefaultRouter
from movielist_app.api.views import WatchListAV, WatchDetailsAV, StreamPlateformAV, StreamPlateformDetailsAV, ReviewList, ReviewDetail, ReviewCreate, StreamPlateformVS

router = DefaultRouter()
router.register('stream', StreamPlateformVS, basename='streamplateform')

urlpatterns = [
    path("list/", WatchListAV.as_view(), name="movie-list"),
    path("<int:pk>/", WatchDetailsAV.as_view(), name='movie-details'),
    
    path('', include(router.urls)),
    
    
    # path("stream/", StreamPlateformAV.as_view(), name="stream-list"),
    # path("stream/<int:pk>", StreamPlateformDetailsAV.as_view(), name="stream-details"),
    
    path("<int:pk>/review-create/", ReviewCreate.as_view(), name='review-create'),
    path("<int:pk>/reviews/", ReviewList.as_view(), name='stream-detail'),
    path("review/<int:pk>/", ReviewDetail.as_view(), name='review-details'),
    
    # path("review/", ReviewList.as_view(), name='review'),
    # path("review/<int:pk>", ReviewDetail.as_view(), name='review-details'),
]