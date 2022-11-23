from django.db import models

# Create your models here.
class WatchListItem(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=500)
    rating = models.IntegerField()
    release_date = models.DateField()
    review = models.TextField()