from django.urls import path
from .views import index, MovieListView, MovieCreateView, DirectorCreateView, MovieUpdateView, DirectorDeleteView, \
    MovieDetailView, MovieDeleteView, ActorCreateView, ActorDeleteView, GenreCreateView, GenreDeleteView

urlpatterns = [
    # path("", index, name="index"),
    path("", MovieListView.as_view(), name="movie-list"),
    path("movie/<int:pk>/", MovieDetailView.as_view(), name="movie-detail"),
    path("movie/create/", MovieCreateView.as_view(), name="movie-create"),
    path(
        "movie/<int:pk>/update/",
        MovieUpdateView.as_view(),
        name="movie-update"
    ),
    path(
        "movie/<int:pk>/delete/",
        MovieDeleteView.as_view(),
        name="movie-delete"
    ),


    path('movie/director/create/', DirectorCreateView.as_view(), name='director-create'),
    path('movie/director/<int:pk>/delete/', DirectorDeleteView.as_view(), name='director-delete'),

    path('movie/actor/create/', ActorCreateView.as_view(), name='actor-create'),
    path('movie/actor/<int:pk>/delete/', ActorDeleteView.as_view(), name='actor-delete'),

    path('movie/genre/create/', GenreCreateView.as_view(), name='genre-create'),
    path('movie/genre/<int:pk>/delete/', GenreDeleteView.as_view(), name='genre-delete'),


]

app_name = "movie"
