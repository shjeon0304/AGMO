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
    description = models.TextField()

class Task(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    progress = models.IntegerField(default=0) 
    

    def __str__(self):
        return self.name
    

