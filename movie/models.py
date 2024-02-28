from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        abstract = True
        unique_together = ("first_name", "last_name")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Director(Person):
    class Meta:
        verbose_name = "Director"
        verbose_name_plural = "Directors"


class Actor(Person):
    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = "Actors"


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    duration = models.CharField(max_length=24)
    genres = models.ManyToManyField(Genre)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return f"{self.title}"
