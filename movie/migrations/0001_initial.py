# Generated by Django 4.2.1 on 2024-03-01 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Actor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("active", models.BooleanField(default=False)),
                ("extra", models.JSONField(blank=True, default=dict)),
                (
                    "upd",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Last Updated"
                    ),
                ),
                ("crt", models.DateTimeField(auto_now=True, verbose_name="Created")),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Director",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("active", models.BooleanField(default=False)),
                ("extra", models.JSONField(blank=True, default=dict)),
                (
                    "upd",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Last Updated"
                    ),
                ),
                ("crt", models.DateTimeField(auto_now=True, verbose_name="Created")),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("active", models.BooleanField(default=False)),
                ("extra", models.JSONField(blank=True, default=dict)),
                (
                    "upd",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Last Updated"
                    ),
                ),
                ("crt", models.DateTimeField(auto_now=True, verbose_name="Created")),
                ("name", models.CharField(max_length=100, unique=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("active", models.BooleanField(default=False)),
                ("extra", models.JSONField(blank=True, default=dict)),
                (
                    "upd",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Last Updated"
                    ),
                ),
                ("crt", models.DateTimeField(auto_now=True, verbose_name="Created")),
                ("title", models.CharField(max_length=100)),
                ("release_year", models.IntegerField()),
                ("duration", models.CharField(default="N/A", max_length=24)),
                ("plot", models.TextField(default="N/A")),
                ("poster_url", models.URLField(blank=True, null=True)),
                ("actors", models.ManyToManyField(to="movie.actor")),
                (
                    "director",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="movie.director",
                    ),
                ),
                ("genres", models.ManyToManyField(to="movie.genre")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddIndex(
            model_name="director",
            index=models.Index(
                fields=["last_name", "first_name"],
                name="movie_direc_last_na_6c3f93_idx",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="director",
            unique_together={("first_name", "last_name")},
        ),
        migrations.AddIndex(
            model_name="actor",
            index=models.Index(
                fields=["last_name", "first_name"],
                name="movie_actor_last_na_c6cfcb_idx",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="actor",
            unique_together={("first_name", "last_name")},
        ),
    ]