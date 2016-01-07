#coding:utf-8#
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser)

from django.utils.html import format_html

import myValidator as myVal
# Create your models here.
class Exuser(models.Model):
    SEX = (
        (0,'男'),
        (1,'女'),
    )
    user         = models.OneToOneField(User)
    phonenum     = models.CharField(max_length=15,null=True,blank=True,help_text="电话号码")
    nickname     = models.CharField(max_length=30,null=True,blank=True,help_text="昵称")
    headimg      = models.ImageField(upload_to='img/headphoto/',null=True,blank=True,help_text="头像")
    sex          = models.IntegerField(choices=SEX,default=0,help_text="性别")
    companyname  = models.CharField(max_length=100,null=True,blank=True,help_text="公司名称")
    boolServer   = models.NullBooleanField(help_text="是否为服务商")
    server       = models.OneToOneField("Servers",null=True,blank=True,help_text="服务商名") 
    inTime       = models.DateTimeField(auto_now=True,auto_now_add=False,help_text="创建时间")    


class Servers(models.Model):
    CLASS = (
        ('0','个人服务商'),
        ('1','企业服务商'),
        ('2','校园服务商'),
    )
    servername    = models.CharField(max_length=100,help_text="服务商名称")
    serverdesc    = models.TextField(help_text="服务商简介")
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
    
    def __unicode__(self):
        return self.modelName

class ClassModel(models.Model):
    className = models.CharField(max_length=50)
    modelName = models.ForeignKey(ServiceModel,related_name="classModel")

    def __unicode__(self):
        return self.className

class Article(models.Model):
    WORK = (
        ('0','需求'),
        ('1','作品'),
    )
    user         = models.ForeignKey(User,help_text='用户名')
    classmodel   = models.ForeignKey(ClassModel,help_text='具体分类')
    servicemodel = models.ForeignKey(ServiceModel,help_text='分类信息')
    title        = models.CharField(max_length=200,help_text='简单介绍')
    content      = models.TextField(help_text='具体要求')
    companyname  = models.CharField(max_length=100,null=True,blank=True,help_text='单位名称')
    price        = models.IntegerField(default=0,null=True,blank=True,help_text='价格')
    img          = models.ImageField(upload_to ='img/article/',null=True,help_text="封面图像",blank=True)
    phonenum     = models.CharField(max_length=15,null=True,blank=True,help_text='电话号码')
    usernickname = models.CharField(max_length=30,null=True,blank=True,help_text='用户昵称（没有设置则显示用户的登陆账户名称）')
    email        = models.EmailField(null=True,blank=True,help_text='邮箱(没有设置则显示用户注册时的邮箱)')
    endDate      = models.DateTimeField(auto_now=False,auto_now_add=False,null=True,blank=True,help_text="结束时间")
    boolIndex    = models.IntegerField(null=True,blank=True,help_text='是否在首页显示(设置为正整数值即可显示，作品可显示8个，需求可显示6个)')
    boolWorks    = models.CharField(max_length=1,choices=WORK,default='0',help_text="需求或者作品")
    insertDate   = models.DateTimeField(auto_now=True,auto_now_add=False,help_text="创建时间")

    class Meta:
        ordering = ['-insertDate']

    
