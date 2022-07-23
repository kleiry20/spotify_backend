from django.db.models import fields
from rest_framework import serializers
from .models import Artist
from songs.serializers import SongSerializer

class ArtistSerializer(serializers.ModelSerializer):
    songs = SongSerializer(read_only=True, many=True)

    class Meta:
        model = Artist
        fields = ('artist_name', 'artist_dob', 'artist_bio')
