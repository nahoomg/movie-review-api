from rest_framework import viewsets
from .models import Movie, Review
from django.contrib.auth.models import User
from .serializers import MovieSerializer, ReviewSerializer, UserSerializer

# This ViewSet will handle all API requests for the Movie model.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# This ViewSet will handle all API requests for the Review model.
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# This ViewSet will handle all API requests for the User model.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer