from django.urls import path

from .views import (
    MovieViewSet,
    ActorViewSet,
    DirectorViewSet,
    GenreViewSet
)

urlpatterns = [
    path("", MovieViewSet.as_view(
        {
            "get": "list",
            "post": "create"
        }
    ), name="movie-list-api"),

    path("<int:pk>/", MovieViewSet.as_view(
        {
            "get": "retrieve",
            "patch": "update",
            "delete": "destroy"
        }
    ), name="movie-detail-api"),

    path("actors/", ActorViewSet.as_view(
        {
            "get": "list",
        }
    ), name="actor-list-api"),

    path("actors/delete/<int:pk>/", ActorViewSet.as_view(
        {
            "delete": "destroy"
        }
    ), name="actor-delete-api"),

    path("directors/", DirectorViewSet.as_view(
        {
            "get": "list",
        }
    ), name="director-list-api"),

    path("directors/delete/<int:pk>/", DirectorViewSet.as_view(
        {
            "delete": "destroy"
        }
    ), name="director-delete-api"),

    path("genres/", GenreViewSet.as_view(
        {
            "get": "list",
        }
    ), name="genres-list-api"),

    path("genres/delete/<int:pk>/", GenreViewSet.as_view(
        {
            "delete": "destroy"
        }
    ), name="genres-delete-api"),
]

app_name = "movie"
