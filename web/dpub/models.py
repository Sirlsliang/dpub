#coding:utf-8#
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser)


# Create your models here.

class Exuser(models.Model):
    IDENTITY = (
        ('0','企业'),
        ('1','学生'),
    )
    SEX = (
        ('0','男'),
        ('1','女'),
    )
    user = models.OneToOneField(User)
    identity = models.CharField(max_length=2,choices=IDENTITY,default='1')
    phonenum = models.IntegerField(null=True,blank=True )
    nickname = models.CharField(max_length=30,null=True,blank=True)
    headimg  = models.ImageField(upload_to='img/headphoto/',null=True,blank=True)
    sex      = models.CharField(max_length=2,choices=SEX,default='0',null=True,blank=True)
    companyname  = models.CharField(max_length=100,null=True,blank=True)
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
    modelImg = models.ImageField(upload_to='img/indexModel/',null=True,blank=True)

class ClassModel(models.Model):
    className = models.CharField(max_length=50)
    modelName = models.ForeignKey(ServiceModel,related_name="classModel")

class Article(models.Model):
    user = models.ForeignKey(User)
    classify = models.ForeignKey(ClassModel)
    title = models.CharField(max_length=200)
    content = models.TextField()
    companyname = models.CharField(max_length=100,null=True,blank=True)
    price   = models.IntegerField(default=0)
    img = models.ImageField(upload_to ='img/article/',null=True,help_text="封面图像",blank=True)
    phonenum  = models.IntegerField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    endDate = models.DateTimeField(auto_now=False,auto_now_add=False)
    insertDate = models.DateTimeField(auto_now=True,auto_now_add=False)

    class Meta:
        ordering = ['-insertDate']
