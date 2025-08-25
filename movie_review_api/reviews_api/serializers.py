from rest_framework import serializers
from .models import Movie, Review
from django.contrib.auth.models import User

# This will convert Movie model data into JSON format.
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

# This will handle the conversion for the Review model.
class ReviewSerializer(serializers.ModelSerializer):
    # A read-only field to display the movie's title instead of its ID.
    movie_title = serializers.ReadOnlyField(source='movie.title')
    # A read-only field to display the username instead of the user's ID.
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Review
        fields = ['id', 'movie', 'user', 'rating', 'comment', 'created_at', 'updated_at', 'movie_title', 'username']

# This serializer will be used for user management.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']