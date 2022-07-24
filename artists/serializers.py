from django.db.models import fields
from rest_framework import serializers
from .models import Artist
from songs.serializers import SongSerializer

class ArtistSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Artist
        fields = ('id', 'artist_name', 'artist_dob', 'artist_bio')
