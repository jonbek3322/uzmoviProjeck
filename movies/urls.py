from django.urls import path
from movies.views import movie_home, movie_detail, movie_form



urlpatterns = [
    path('', movie_home),
    path('<int:movie_id>/', movie_detail),
    path('create/', movie_form)
]
