from django.db import models
from app_users.models import AppUser

# Create your models here.  
class Rating(models.Model):
    id = models.IntegerField(primary_key=True)
    app_user = models.ForeignKey(AppUser, null=True, blank=True, on_delete=models.SET_NULL)
    rating = models.FloatField(max_length=255)
  
    def __str__(self) -> str:
        return str(self.id)