from django.db import models
from artists.models import Artist

# Create your models here.  
class AppUser(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
  
    def __str__(self) -> str:
        return self.name