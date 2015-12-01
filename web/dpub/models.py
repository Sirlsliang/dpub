#coding:utf-8#
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Exuser(models.Model):
    IDENTITY = (
        ('0','企业'),
        ('1','学生'),
    )
    user = models.OneToOneField(User)
    identity = models.CharField(max_length=2,choices=IDENTITY,default='1')
    inTime   = models.DateTimeField(auto_now=True,auto_now_add=False)    


class School(models.Model):
    schName = models.CharField(max_length=100)
    schDesc = models.TextField()
    schUrl  = models.URLField()
    schLogo = models.ImageField(upload_to='img/schoolLogo/')

class Course(models.Model):
    courName = models.CharField(max_length=50)
    school   = models.ForeignKey(School)

class ServiceModel(models.Model):
    modelName = models.CharField(max_length=50)
    modelImg = models.ImageField(upload_to='img/indexModel',null=True,blank=True)

class ClassModel(models.Model):
    className = models.CharField(max_length=50)
    modelName = models.ForeignKey(ServiceModel,related_name="classModel")
