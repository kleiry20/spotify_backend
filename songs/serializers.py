from rest_framework import serializers

from artists.models import Artist
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    artist = serializers.PrimaryKeyRelatedField(queryset=Artist.objects.all(),
                                                  many=False) 
    class Meta:
        model = Song
        fields = ('name', 'artist', 'date_of_release', "avg_rating", 'id','image',)
