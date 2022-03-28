import re
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http.response import HttpResponse, Http404
from movies.models import Movie
from movies.forms import MovieForm

# Create your views here.


def movie_form(request):
    form=MovieForm()
    errors = {}
    data = {}
    # return render(request=request,template_name='movie_create.html', content_type={'form':form})
    # form = MovieForm()
    # print("salom")

    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/create/')

    return(request, 'movie_create.html', {'errors': errors, 'data': data, 'form': form})



def movie_home(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movie_home.html', context)


def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    context = {
        'movie': movie
    }
    return render(request, 'movie_detail.html', context)