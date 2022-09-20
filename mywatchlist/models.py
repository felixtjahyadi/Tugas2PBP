from django.db import models

# Create your models here.
class WatchListItem(models.Model):
    watched = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    rating = models.IntegerField()
    release_date = models.CharField(max_length=500)
    review = models.TextField()