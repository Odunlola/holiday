from django.urls import path
from .import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('destinations/', views.DestinationList.as_view(), name="destination_list"),
    path('spots/', views.SpotList.as_view(), name="spot_list"),
    path('destinations/new/', views.DestinationCreate.as_view(), name="destination_create"),
    path('destinations/<int:pk>/', views.DestinationDetail.as_view(), name="destination_detail"),
    path('destinations/<int:pk>/update', views.DestinationUpdate.as_view(), name="destination_update"),
    path('destinations/<int:pk>/delete', views.DestinationDelete.as_view(), name="destination_delete"),
    path('destinations/<int:pk>/songs/new', views.SpotCreate.as_view(), name="spot_create"),
    path('lists/<int:pk>/songs/<int:song_pk>/', views.ListAssoc.as_view(), name="list_spot_assoc"),
]
