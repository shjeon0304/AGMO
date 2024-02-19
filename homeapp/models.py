from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Crop(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length = 255)

    def __str__(self):
        return self.name


class Farmland(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    land = models.CharField(max_length = 100)

    def __str__(self):
        return self.land


class Task(models.Model):
    land = models.ForeignKey(Farmland, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length = 255)
    progress = models.IntegerField()
    start_date = models.DateField()
    Finish_date = models.DateField()

    def __str__(self):
        return self.name
    

