from rest_framework import serializers

from ..models import Actor, Director, Genre, Movie


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "first_name",
            "last_name"
        )


class ActorSerializer(PersonSerializer):
    class Meta(PersonSerializer.Meta):
        model = Actor


class DirectorSerializer(PersonSerializer):
    class Meta(PersonSerializer.Meta):
        model = Director


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            "id",
            "name",
        )


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = (
            "active",
            "extra",
            "upd",
            "crt"
        )


class MovieDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    director = DirectorSerializer()
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = (
            "title",
            "release_year",
            "duration",
            "plot",
            "poster_url",
            "actors",
            "director",
            "genres",
            "crt",
            "upd"
        )
