from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User

class StreamPlatform(models.Model):
    name=models.CharField(max_length=30)
    about=models.CharField(max_length=150)
    website=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

# Create your models here.
class Watchlist(models.Model):
    title=models.CharField(max_length=50)
    storyline=models.CharField(max_length=200)
    platform=models.ForeignKey(StreamPlatform,on_delete=models.CASCADE,related_name='watchlist')
    active=models.BooleanField(default=True)
    avg_rating=models.FloatField(default=0)
    number_rating=models.IntegerField(default=0)
    created=models.DateTimeField(auto_now_add=True)
    
    def _str_(self):
        return self.name

class Review(models.Model):
    review_user=models.ForeignKey(User,on_delete=models.CASCADE)
    ratings=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.CharField(max_length=200,null=True)
    watchlist=models.ForeignKey(Watchlist,on_delete=models.CASCADE,related_name="reviews")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.ratings)


#? currently on video 41 token authentication