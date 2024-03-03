from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Actor, Director, Movie, Genre

admin.site.unregister(Group)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "active", "upd", "crt")


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'release_year', 'duration', 'plot', 'poster_url', 'director'
    )
