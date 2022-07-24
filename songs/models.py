from email.policy import default
from django.db import models
from django.forms import NullBooleanField
from artists.models import Artist

# Create your models here.  
class Song(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    date_of_release = models.DateTimeField(auto_now_add=True)
    artist = models.ForeignKey(Artist, null=True, blank=True, on_delete=models.SET_NULL)
    avg_rating = models.FloatField(max_length=255)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self) -> str:
        return self.name