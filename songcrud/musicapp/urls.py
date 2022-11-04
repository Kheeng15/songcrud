from django.urls import path

from .views import Artiste_listAPIView, Artiste_detailsAPIView, Song_listAPIView, Song_detailsAPIView


urlpatterns = [
    
    path('artiste_list/', Artiste_listAPIView.as_view()),
    path('artiste_details/<int:id>', Artiste_detailsAPIView.as_view()),
    path('song_list/', Song_listAPIView.as_view()),
    path('song_details/<int:id>', Song_detailsAPIView.as_view()),

    
]