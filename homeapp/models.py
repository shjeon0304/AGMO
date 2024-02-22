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


class Cropdata(models.Model):
    CROP_CHOICES = {
        ('팥','팥'),
        ('밀','밀')
    }
    CROPWORK_CHOICES = {
        ('파종','파종'),
        ('제초','제초'),
        ('배수구 정비','배수구 정비'),
        ('토입','토입'),
        ('답압','답압'),
        ('추비','추비'),
        ('방제','방제'),
        ('수확및 탈곡','수확및 탈곡'),
        ('수매','수매'),
        ('북주기','북주기'),
        ('김매기','김매기'),
        ('배수작업','배수작업'),
        ('수확','수확'),
    }
    PESTICIDE_CHOICES = {
        ('알라코입제','알라코입제'),
        ('파라코입제','파라코입제'),
        ('부타유제','부타유제'),
        ('수화유황','수화유황'),
        ('두엄','두엄'),
        ('적미방제약','적미방제약')
    }
    crop = models.CharField(max_length=50, choices=CROP_CHOICES)
    fieldNum = models.IntegerField()
    cropWork = models.CharField(max_length=50, choices=CROPWORK_CHOICES)
    pesticide = models.CharField(max_length=50, choices=PESTICIDE_CHOICES) 
    date = models.DateTimeField()
    content = models.CharField(max_length=4000)

    def __str__(self):
        return self.title

'''class Cropdiary(models.Model):
    
    CROP_CHOIECES = {
        ('red-bean','팥'),
        ('wheat','밀')

    }


    crop = models.CharField(max_length=80, choilces=CROP_CHOICES, null=True)

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"username": self.username})
'''

