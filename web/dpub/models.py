from django.db import models


# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email    = models.EmailField(max_length=50)
    inTime   = models.DateTimeField(auto_now=True,auto_now_add=False)
    


class School(models.Model):
    schName = models.CharField(max_length=100)
    schDesc = models.TextField()
    schUrl  = models.URLField()
    schLogo = models.ImageField(upload_to='img/schoolLogo/')

class Course(models.Model):
    courName = models.CharField(max_length=50)
    school   = models.ForeignKey(School)
