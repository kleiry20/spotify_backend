from rest_framework import serializers

from .models import AppUser

class AppUserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = AppUser
        fields = ('name', 'id', )
