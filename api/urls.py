from django.urls import path

from api import views

urlpatterns = [
    path('register/', views.register_address, name='register'),
    path('get_all_address/', views.get_all_address, name='get_all_location'),
    path('get_location/', views.get_location, name='get_location'),
    path('delete_by_id<int:pk>/', views.delete_by_id, name='delete_by_id'),
]


