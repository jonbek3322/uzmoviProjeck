
from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ['title', 'language', 'released_year', 'duration', 'country', 'source_link', 'banner',
        'category_id', 'slug', 'type']