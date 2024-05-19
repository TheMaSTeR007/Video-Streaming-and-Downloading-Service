from django.db import models

# Create your models here.

class FilmDetails(models.Model):
    video_field = models.FileField(upload_to='static/media/AllFilms', max_length=500, editable=True)
    # video_shortDesc = models.TextField(max_length=50, default='video short description')
    video_desc = models.TextField(max_length=500, editable=True)
    # duration = models.CharField(max_length=20)
    released_year = models.IntegerField(default=2024, editable=True)
    thumbnail=models.FileField(upload_to='static/media/AllFilms/thumbnails',default='thumbnails/tn.jpeg', editable=True)
    title=models.CharField(max_length=150,default='movie title', editable=True)
    ratings = models.IntegerField(default=0, editable=True)

class Movies(models.Model):
    video_field = models.FileField(upload_to='static/media/AllMovies', editable=True)
    # video_shortDesc = models.TextField(max_length=50, default='video short description')
    video_desc = models.TextField(max_length=500, editable=True)
    # duration = models.CharField(max_length=20)
    released_year = models.IntegerField(default=2024, editable=True)
    thumbnail=models.FileField(upload_to='static/media/AllMovies/thumbnails',default='thumbnails/tn.jpeg', editable=True)
    title=models.CharField(max_length=150,default='movie title', editable=True)
    ratings = models.IntegerField(default=0, editable=True)
    film_details = models.OneToOneField(FilmDetails, on_delete=models.CASCADE, primary_key=True, editable=True)

class Webseries(models.Model):
    video_field = models.FileField(upload_to='static/media/Webseries', editable=True)
    # video_shortDesc = models.TextField(max_length=50, default='video short description')
    video_desc = models.TextField(max_length=500, editable=True)
    # duration = models.CharField(max_length=20)
    released_year = models.IntegerField(default=2024, editable=True)
    thumbnail=models.FileField(upload_to='static//media/Webseries/thumbnails',default='thumbnails/tn.jpeg', editable=True)
    title=models.CharField(max_length=150,default='movie title', editable=True)
    ratings = models.IntegerField(default=0, editable=True)
    film_details = models.OneToOneField(FilmDetails, on_delete=models.CASCADE, primary_key=True, editable=True)

class Bollywood(models.Model):
    video_field = models.FileField(upload_to='static/media/Bollywood', editable=True)
    # video_shortDesc = models.TextField(max_length=50, default='video short description')
    video_desc = models.TextField(max_length=500, editable=True)
    # duration = models.CharField(max_length=20)
    released_year = models.IntegerField(default=2024, editable=True)
    thumbnail=models.FileField(upload_to='static/Bollywood/thumbnails',default='thumbnails/tn.jpeg', editable=True)
    title=models.CharField(max_length=150,default='movie title', editable=True)
    ratings = models.IntegerField(default=0, editable=True)
    film_details = models.OneToOneField(FilmDetails, on_delete=models.CASCADE, primary_key=True, editable=True)

class Hollywood(models.Model):
    video_field = models.FileField(upload_to='static/media/Hollwood', editable=True)
    # video_shortDesc = models.TextField(max_length=50, default='video short description')
    video_desc = models.TextField(max_length=500, editable=True)
    # duration = models.CharField(max_length=20)
    released_year = models.IntegerField(default=2024, editable=True)
    thumbnail=models.FileField(upload_to='static/Hollywood/thumbnails',default='thumbnails/tn.jpeg', editable=True)
    title=models.CharField(max_length=150,default='movie title', editable=True)
    ratings = models.IntegerField(default=0, editable=True)
    film_details = models.OneToOneField(FilmDetails, on_delete=models.CASCADE, primary_key=True, editable=True)
