from django.db import models


class BaseModel(models.Model):
    active = models.BooleanField(default=False)

    extra = models.JSONField(blank=True, default=dict)
    upd = models.DateTimeField(
        verbose_name='Last Updated',
        auto_now_add=True,
    )
    crt = models.DateTimeField(
        verbose_name='Created',
        auto_now=True,
    )

    class Meta:
        abstract = True


class Person(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        abstract = True
        unique_together = ("first_name", "last_name")

        indexes = [
            models.Index(fields=["last_name", "first_name"]),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Director(Person):
    pass


class Actor(Person):
    pass


class Genre(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"


class Movie(BaseModel):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    duration = models.CharField(max_length=24, default="N/A")
    plot = models.TextField(default="N/A")
    poster_url = models.URLField(blank=True, null=True)

    genres = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actor)

    director = models.ForeignKey(Director, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.title}"
