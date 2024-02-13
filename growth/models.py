from django.db import models

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
    
#Class Proper_date() 만들어서 작업별로 추천 일자 나타내고 일지쓸때랑 연계하자 이건 나중에 ㅠ


