from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import FavouriteDog
from .serializers import FavouriteDogSerializer

@api_view(['GET', 'POST'])
def check_favourite_dog(request, link):
    try:
        favourite_dog = FavouriteDog.objects.get(link=link)
        exists = True
    except FavouriteDog.DoesNotExist:
        exists = False

    return Response({'favourite': exists})

@api_view(['GET', 'POST'])
def get_favourite_dogs(request):
    favourite_dogs = FavouriteDog.objects.all()
        
    serialized_favourite_dogs = FavouriteDogSerializer(favourite_dogs, many=True)
    return Response(serialized_favourite_dogs.data)

@api_view(['GET', 'POST'])
def add_favourite_dog(request, link):
  if request.method == 'POST':
        FavouriteDog.objects.create(link=link)

  return Response({'new fav dog': link})

@api_view(['GET', 'POST'])
def remove_favourite_dog(request, link):
  if request.method == 'POST':
    try:
        favourite_dog = FavouriteDog.objects.get(link=link)
    except FavouriteDog.DoesNotExist:
        raise Http404()
    favourite_dog.delete()

  return Response({'removed fav dog': link})
