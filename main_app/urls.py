from django.urls import path
from .import views

# app_name = "main" 

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
    path('destinations/<int:pk>/spots/new', views.SpotCreate.as_view(), name="spot_create"),
    path('lists/<int:pk>/spots/<int:spot_pk>/', views.ListAssoc.as_view(), name="list_spot_assoc"),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name= "logout"),
]
