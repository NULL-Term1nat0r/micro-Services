from django.urls import path
from .views import clock, get_time

urlpatterns = [
    path('', clock, name='clock'),
    path('get_time/', get_time, name='get_time'),
]


