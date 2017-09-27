from django.db import models

# Create your models here.
class Movie(models.Model):
	actor=models.CharField(max_length=10)  
	actor_movie=models.CharField(max_length=20) 
	genre=models.CharField(max_length=30)
	movie_logo=models.CharField(max_length=40)

	"""def __str__(self):
		return str(self.id)+"  "+self.actor+'----'+self.actor_movie+'----'+self.genre+'----'+self.movie_logo+''"""		