from django.shortcuts import render
from django import forms
from appmodel.forms import MyMovieForm
from .models import Movie
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def add_model(request):
	
	if request.method == "POST":
		form = MyMovieForm(request.POST)
		if form.is_valid():
			n2 = form.save()
			n2.save()
			actor=request.POST.get('actor')
			actor_movie=request.POST.get('actor_movie')
			genre=request.POST.get('genre')
			movie_logo=request.POST.get('movie_logo')
			context={'actor': actor, 'actor_movie': actor_movie, 'genre': genre, 'movie_logo': movie_logo}
		return render(request,"fetch.html", context)
	else:
		form = MyMovieForm()
		return render(request,"insert.html",{'form':form})