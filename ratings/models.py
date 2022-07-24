from django.db import models
from django.db.models import Sum
from app_users.models import AppUser
from songs.models import Song

# Create your models here.  
class Rating(models.Model):
    id = models.IntegerField(primary_key=True)
    app_user = models.ForeignKey(AppUser, null=True, blank=True, on_delete=models.SET_NULL)
    song = models.ForeignKey(Song, null=True, blank=True, on_delete=models.SET_NULL)
    rating = models.FloatField(max_length=255)

    def update_rating(self):
        ratings = Rating.objects.filter(song=self.song.id)
        total_ratings = ratings.aggregate(Sum('rating'))
        count = ratings.count()
        song = self.song
        song.avg_rating = total_ratings['rating__sum'] // count
        print(song, total_ratings['rating__sum'] // count)
        song.save()

    def update_artist_rating(self):
        artist = self.song.artist
        ratings = Song.objects.filter(artist=artist.id)
        total_ratings = ratings.aggregate(Sum('avg_rating'))
        count = ratings.count()
        artist.avg_rating = total_ratings['avg_rating__sum'] // count
        artist.save()
  
    def __str__(self) -> str:
        return str(self.id)