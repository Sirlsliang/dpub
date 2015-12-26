#coding:utf-8#
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser)


# Create your models here.

class Exuser(models.Model):
    SEX = (
        (0,'男'),
        (1,'女'),
    )
    user         = models.OneToOneField(User)
    phonenum     = models.CharField(max_length=15,null=True,blank=True )
    nickname     = models.CharField(max_length=30,null=True,blank=True)
    headimg      = models.ImageField(upload_to='img/headphoto/',null=True,blank=True)
    sex          = models.IntegerField(choices=SEX,default=0,null=True,blank=True)
    companyname  = models.CharField(max_length=100,null=True,blank=True)
    boolServer   = models.NullBooleanField()
    server       = models.OneToOneField("Servers",null=True,blank=True) 
    inTime       = models.DateTimeField(auto_now=True,auto_now_add=False)    


class Servers(models.Model):
    CLASS = (
        ('0','个人服务商'),
        ('1','企业服务商'),
        ('2','校园服务商'),
    )
    servername    = models.CharField(max_length=100)
    serverdesc    = models.TextField()
    serverurl     = models.URLField()
    serverlogo    = models.ImageField(null=True,blank=True,upload_to='img/serverlogo/')
    serverbanner  = models.ImageField(null=True,blank=True,upload_to='img/serverbanner/')
    serverclass   = models.CharField(max_length=2,choices=CLASS,default='0')
    servertel     = models.CharField(max_length=12,null=True,blank=True)
    serveraddress = models.CharField(max_length=100,null=True,blank=True)

class Lesson(models.Model):
    lessonname = models.CharField(max_length=50)
    server     = models.ForeignKey(Servers,related_name="lessonModel")

class ServiceModel(models.Model):
    modelName = models.CharField(max_length=50)
    modelImg  = models.ImageField(upload_to='img/indexModel/',null=True,blank=True)

class ClassModel(models.Model):
    className = models.CharField(max_length=50)
    modelName = models.ForeignKey(ServiceModel,related_name="classModel")

class Article(models.Model):
    WORK = (
        ('0','需求'),
        ('1','作品'),
    )
    user         = models.ForeignKey(User)
    classmodel   = models.ForeignKey(ClassModel)
    servicemodel = models.ForeignKey(ServiceModel)
    title        = models.CharField(max_length=200)
    content      = models.TextField()
    companyname  = models.CharField(max_length=100,null=True,blank=True)
    price        = models.IntegerField(default=0,null=True,blank=True)
    img          = models.ImageField(upload_to ='img/article/',null=True,help_text="封面图像",blank=True)
    phonenum     = models.CharField(max_length=15,null=True,blank=True)
    usernickname = models.CharField(max_length=30,null=True,blank=True)
    email        = models.EmailField(null=True,blank=True)
    endDate      = models.DateTimeField(auto_now=False,auto_now_add=False,null=True,blank=True)
    boolIndex    = models.IntegerField(null=True,blank=True)
    boolWorks    = models.CharField(max_length=1,choices=WORK,default='0')
    insertDate   = models.DateTimeField(auto_now=True,auto_now_add=False)

    class Meta:
        ordering = ['-insertDate']
