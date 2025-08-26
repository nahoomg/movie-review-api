
from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import Movie, Review
from django.contrib.auth.models import User
from .serializers import MovieSerializer, ReviewSerializer, UserSerializer, UserCreateSerializer


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


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # This ensures only authenticated users can manage reviews
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # This makes sure a review's user is automatically set to the logged-in user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # This makes sure users can only update their own reviews
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Review.objects.filter(user=user)
        return Review.objects.all()

@api_view(['POST'])
def register_user(request):
    serializer = UserCreateSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'username': user.username}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'username': user.username}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)