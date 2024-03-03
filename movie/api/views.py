from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import (
    ActorSerializer,
    MovieDetailSerializer,
    MovieSerializer,
    DirectorSerializer,
    GenreSerializer
)
from ..filters import MovieFilter
from ..models import Movie, Actor, Director, Genre


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.select_related(
        "director"
    ).prefetch_related("actors", "genres")
    filter_backends = [DjangoFilterBackend]
    filterset_class = MovieFilter

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MovieDetailSerializer
        return MovieSerializer
