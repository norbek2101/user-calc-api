from rest_framework import serializers
from .models import UserProfile, Place  # Assuming models UserProfile and Place exist

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'name', 'country', 'region', 'district', 'users')  # Adjust fields as needed

class UserProfileSerializer(serializers.ModelSerializer):
    place = PlaceSerializer()  # Serialize the related Place model

    class Meta:
        model = UserProfile
        fields = ('id', 'name', 'age')