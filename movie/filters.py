from django_filters import FilterSet, NumberFilter, ModelChoiceFilter
from .models import Director, Actor, Movie


class MovieFilter(FilterSet):
    release_year = NumberFilter(lookup_expr='exact')
    director = ModelChoiceFilter(queryset=Director.objects.all())
    actors = ModelChoiceFilter(queryset=Actor.objects.all())

    class Meta:
        model = Movie
        fields = ['release_year', 'director', 'actors']
