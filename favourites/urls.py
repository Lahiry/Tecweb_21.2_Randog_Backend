from django.urls import path

from . import views

urlpatterns = [
    path('api/favourites/check/<path:link>/', views.check_favourite_dog),
    path('api/favourites/create/<path:link>/', views.add_favourite_dog),
    path('api/favourites/remove/<path:link>/', views.remove_favourite_dog),
    path('api/favourites/', views.get_favourite_dogs)
]