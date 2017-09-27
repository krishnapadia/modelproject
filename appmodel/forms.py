from django.forms import ModelForm
from appmodel.models import Movie

class MyMovieForm(ModelForm):
	class Meta:
		model=Movie
		fields=['actor', 'actor_movie', 'genre', 'movie_logo'] 