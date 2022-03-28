from unicodedata import category
from django import views
from django.db import models

# Create your models here.
class Movie(models.Model):

    class TYPE:

        MOVIE = 'MOVIE'
        TRAILER = 'TRAILER'
        SHOW = 'SHOW'
        SERIES = 'SERIES'


        CHOICE = (
            (MOVIE, MOVIE),
            (TRAILER, TRAILER),
            (SHOW, SHOW),
            (SERIES, SERIES)
        )


    title = models.CharField(max_length=150)
    language = models.CharField(max_length=50, default="O'zbek tilida")
    released_year = models.IntegerField(null=True)
    duration = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    source_link = models.URLField(max_length=200)
    banner = models.ImageField(upload_to='banners', null=True)
    views_count = models.IntegerField(default=0)
    category_id = models.IntegerField(null=True)
    created_add = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250)
    modified_at = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=7, choices=TYPE.CHOICE, default=TYPE.MOVIE)

    def __str__(self) -> str:
        return self.title