from django.db import models

# Create your models here.


class MovieGenre(models.Model):
    movieGenre_id = models.CharField(max_length=10, blank=True)
    movieGenre_name = models.CharField(max_length=100, blank=True)

    class Meta:
        app_label = 'hub'

    def __str__(self):
        return self.movieGenre_name


class Movie(models.Model):
    tmdb_id = models.IntegerField(null=True)
    movieTitle = models.CharField(max_length=300, blank=True)
    movieRelYear = models.CharField(max_length=4, blank=True)
    moviePoster = models.CharField(max_length=200, blank=True)
    movieBackDrop = models.CharField(max_length=200, blank=True)
    movieOverview = models.CharField(max_length=2000, blank=True)
    movieRuntime = models.CharField(max_length=10, blank=True)
    genres = models.ManyToManyField(MovieGenre, blank=True)

    class Meta:
        app_label = 'hub'

    def __str__(self):
        return self.movieTitle
