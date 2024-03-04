from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from .forms import (
    MovieCreateForm,
    ActorCreateForm,
    DirectorCreateForm,
    GenreCreateForm
)
from .models import Movie, Actor, Director, Genre
from .filters import MovieFilter


def index(request):
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_visits": num_visits + 1,
    }

    return render(request, "index.html", context=context)


class MovieListView(generic.ListView):
    model = Movie
    filterset_class = MovieFilter

    paginate_by = 25

    def get_queryset(self):
        queryset = super().get_queryset().prefetch_related(
            "actors", "genres"
        ).select_related("director")
        self.filterset = self.filterset_class(
            self.request.GET,
            queryset=queryset
        )
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


class MovieCreateUpdateMixin:
    model = Movie
    form_class = MovieCreateForm
    success_url = reverse_lazy("movie:movie-list")


class MovieCreateView(MovieCreateUpdateMixin, generic.CreateView):
    pass


class MovieUpdateView(MovieCreateUpdateMixin, generic.UpdateView):
    pass


class MovieDeleteView(generic.DeleteView):
    model = Movie
    success_url = reverse_lazy("movie:movie-list")


class BaseCreateListView(generic.ListView):
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class()
        return context

    def post(self, request, **kwargs):
        first_name = request.POST.get("first_name", None)
        last_name = request.POST.get("last_name", None)

        if first_name and last_name:
            self.model.objects.create(
                first_name=first_name,
                last_name=last_name
            )
        return redirect(self.success_url)


class DirectorListView(BaseCreateListView):
    model = Director
    form_class = DirectorCreateForm
    success_url = reverse_lazy("movie:director-list")


class DirectorCreateView(generic.CreateView):
    model = Director
    form_class = DirectorCreateForm
    success_url = reverse_lazy("movie:movie-create")


class DirectorDeleteView(generic.DeleteView):
    model = Director
    success_url = reverse_lazy("movie:director-list")


class ActorListView(BaseCreateListView):
    model = Actor
    form_class = ActorCreateForm
    success_url = reverse_lazy("movie:actor-list")


class ActorCreateView(generic.CreateView):
    model = Actor
    form_class = ActorCreateForm
    success_url = reverse_lazy("movie:movie-create")


class ActorDeleteView(generic.DeleteView):
    model = Actor
    success_url = reverse_lazy("movie:actor-list")


class GenreListView(BaseCreateListView):
    model = Genre
    form_class = GenreCreateForm
    success_url = reverse_lazy("movie:genre-list")

    def post(self, request, **kwargs):
        name = request.POST.get("name", None)
        if name:
            self.model.objects.create(name=name)
        return redirect(self.success_url)


class GenreCreateView(generic.CreateView):
    model = Genre
    form_class = GenreCreateForm
    success_url = reverse_lazy("movie:movie-create")


class GenreDeleteView(generic.DeleteView):
    model = Genre
    success_url = reverse_lazy("movie:genre-list")
