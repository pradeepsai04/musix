from django.db import models

# Create your models here.

class upload(models.Model):
    video=models.FileField(upload_to="videos/",default="NULL")
    def __str__(self):
        return "pradeep"


class data(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()