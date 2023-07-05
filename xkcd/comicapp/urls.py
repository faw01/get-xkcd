from django.urls import path
from .views import get_random_comic, get_previous_comic, get_next_comic

urlpatterns = [
    path('api/get_random_comic', get_random_comic, name='random_comic'),
    path('api/get_previous_comic', get_previous_comic, name='previous_comic'),
    path('api/get_next_comic', get_next_comic, name='next_comic'),
]
