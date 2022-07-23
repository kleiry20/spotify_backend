from django.db import models

# Create your models here.  
class Artist(models.Model):
    id = models.IntegerField(primary_key=True)
    artist_name = models.CharField(max_length=255)
    artist_dob = models.DateField()
    artist_bio = models.CharField(max_length=255)
  
    def __str__(self) -> str:
        return self.artist_name