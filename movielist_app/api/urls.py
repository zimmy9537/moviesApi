from django.urls import path, include
# from movielist_app.api.views import movie_list,movie_details
from movielist_app.api.views import ReviewCreate, ReviewDetails, StreamDetailsAV, WatchListAV,WatchDetailAV,StreamPlatformAV,ReviewList

urlpatterns = [
    path('list/',WatchListAV.as_view(),name='movie-list'),
    path('<int:pk>/',WatchDetailAV.as_view(),name='movie-details'),
    path('stream/',StreamPlatformAV.as_view(),name='stream-list'),
    path('stream/<int:pk>/',StreamDetailsAV.as_view(),name='stream-details'),
    
    # path('reviews',ReviewList.as_view(),name='review-list'),
    # path('review/<int:pk>',ReviewDetails.as_view(),name='review-details')
    
    # path('stream/<int:pk>/review-create',ReviewCreate.as_view(),name='review-create'),
    # path('stream/review/<int:pk>',ReviewDetails.as_view(),name='review-detail'),
    # path('stream/<int:pk>/review',ReviewList.as_view(),name='review-list')
    
    path('<int:pk>/review-create/',ReviewCreate.as_view(),name='review-create'),
    path('<int:pk>/reviews/',ReviewList.as_view(),name='review-list'),
    path('review/<int:pk>/',ReviewDetails.as_view(),name='review-detail')
]