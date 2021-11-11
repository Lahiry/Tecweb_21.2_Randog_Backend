from rest_framework import serializers
from .models import FavouriteDog


class FavouriteDogSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouriteDog
        fields = ['id', 'link']