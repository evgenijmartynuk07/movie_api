from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import MovieCreateForm, PersonCreateForm, ActorCreateForm, DirectorCreateForm, GenreCreateForm
from .models import Movie, Actor, Director, Genre
from .filters import MovieFilter


def index(request):
    return {}


class MovieListView(generic.ListView):
    model = Movie
    filterset_class = MovieFilter

    paginate_by = 25

    def get_queryset(self):
        queryset = super().get_queryset().select_related(
        ).prefetch_related(
            "actors",
        ).select_related("director")
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context


class MovieDetailView(generic.DetailView):
    model = Movie
    queryset = Movie.objects.prefetch_related(
        "actors", "genres"
    ).select_related(
        "director"
    )


class MovieCreateView(generic.CreateView):
    model = Movie
    form_class = MovieCreateForm
    success_url = reverse_lazy("movie:movie-list")


class MovieUpdateView(generic.UpdateView):
    model = Movie
    form_class = MovieCreateForm
    success_url = reverse_lazy("movie:movie-list")


class MovieDeleteView(generic.DeleteView):
    model = Movie


class DirectorCreateView(generic.CreateView):
    model = Director
    form_class = DirectorCreateForm
    success_url = reverse_lazy("movie:movie-create")


class DirectorDeleteView(generic.DeleteView):
    model = Director


class ActorCreateView(generic.CreateView):
    model = Actor
    form_class = ActorCreateForm
    success_url = reverse_lazy("movie:movie-create")


class ActorDeleteView(generic.DeleteView):
    model = Actor


class GenreCreateView(generic.CreateView):
    model = Genre
    form_class = GenreCreateForm
    success_url = reverse_lazy("movie:movie-create")


class GenreDeleteView(generic.DeleteView):
    model = Genre
