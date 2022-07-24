from rest_framework import serializers

from app_users.models import AppUser
from songs.models import Song
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    app_user = serializers.PrimaryKeyRelatedField(queryset=AppUser.objects.all(),
                                                  many=False) 
    song = serializers.PrimaryKeyRelatedField(queryset=Song.objects.all(),
                                                  many=False)
    id = serializers.ReadOnlyField()
    class Meta:
        model = Rating
        fields = ('app_user', "rating", "song", "id")
