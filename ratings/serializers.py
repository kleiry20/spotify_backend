from rest_framework import serializers

from app_users.models import AppUser
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    app_user = serializers.PrimaryKeyRelatedField(queryset=AppUser.objects.all(),
                                                  many=False) 
    class Meta:
        model = Rating
        fields = ('app_user', "rating")
