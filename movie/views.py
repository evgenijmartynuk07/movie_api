from django.shortcuts import render
from django.views import generic
from .models import Movie, Actor
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



