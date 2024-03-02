from django import forms
from .models import Movie, Director, Actor, Genre


class GenreCreateForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ("name",)


class PersonCreateForm(forms.ModelForm):
    class Meta:
        abstract = True
        fields = ("first_name", "last_name")


class DirectorCreateForm(PersonCreateForm):
    class Meta(PersonCreateForm.Meta):
        model = Director


class ActorCreateForm(PersonCreateForm):
    class Meta(PersonCreateForm.Meta):
        model = Actor


class MovieCreateForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = (
            'title',
            'release_year',
            'duration',
            'plot',
            'poster_url',
            'genres',
            'actors',
            'director'
        )

