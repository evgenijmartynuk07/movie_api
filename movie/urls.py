from django.urls import path
from .views import index, MovieListView

urlpatterns = [
    # path("", index, name="index"),
    path("", MovieListView.as_view(), name="movie-list")

]

app_name = "movie"