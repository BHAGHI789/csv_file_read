from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_csv, name='upload_csv'),
    path('download/<str:new_file_name>/', views.download_csv, name='download_csv'),
]