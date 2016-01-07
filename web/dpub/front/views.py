#coding:utf-8#
import os
from datetime import *
from django.conf import settings
from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect

from django.views.generic import View,ListView,DetailView
from django.views.generic import TemplateView

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,Group

from django.contrib.auth.decorators import login_required,permission_required
from django.utils.decorators import method_decorator

from dpub.models import *
from dpub.forms import * 

from dpub.conf import *

# Create your views here.
class IndexView(View):
    def get(self,request):
        allServiceModel = ServiceModel.objects.all()
        articles = Article.objects.order_by('boolIndex').filter(boolWorks="0").filter(boolIndex__gte=0).filter(endDate__gte=datetime.today())
        indexWorks = Article.objects.order_by('boolIndex').filter(boolWorks="1").filter(boolIndex__gte=0)
        return render(request,'dpub/index.html',{'allServiceModel':allServiceModel,'articles':articles,'indexWorks':indexWorks,"navigator":"1"})

class ContactUsView(TemplateView):
    template_name ="dpub/contact-us.html"

class ServersView(View):
    def get(self,request):
        allServiceModel = ServiceModel.objects.all()
        servers = Servers.objects.all()
        schoolServers = servers.filter(serverclass='2')
        comServers = servers.filter(serverclass='1')
        personServers = servers.filter(serverclass='0')
        return render(request,'dpub/servers.html',{'servers':servers,'allServiceModel':allServiceModel,"schoolServers":schoolServers,"comServers":comServers,"personServers":personServers,"navigator":"3"})

def server(request,pk):
    allServiceModel = ServiceModel.objects.all()
    server = Servers.objects.get(pk =pk)
    lessons = server.lessonModel.all()
    return render(request,"dpub/tust.html",{"allServiceModel":allServiceModel,"server":server,"lessons":lessons,"navigator":3})

                        

def serviceModelArticles(request,serviceModelId):
    allServiceModel = ServiceModel.objects.all()
    serviceModel = ServiceModel.objects.get(pk=serviceModelId)
    return render(request,'dpub/articles.html',{"allServiceModel":allServiceModel,"serviceId":serviceModelId,"serviceModel":serviceModel,"navigator":"2"})

def classModelArticles(request,serviceModelId,classModelId):
    serviceModel = ServiceModel.objects.get(pk=serviceModelId)
    classModel = serviceModel.classModel.get(pk=classModelId)
    allServiceModel = ServiceModel.objects.all()
    return render(request,'dpub/articles.html',{"allServiceModel":allServiceModel,"serviceModel":serviceModel,"classModel":classModel,"navigator":"2"})


def articleDetail(request,articleId):
    allServiceModel = ServiceModel.objects.all()
    article = get_object_or_404(Article,pk=articleId)
    return render(request,'dpub/article-detail.html',{"allServiceModel":allServiceModel,'article':article})

def serviceArticle(request,serviceModelId,pageId):
    articleList = Article.objects.filter(servicemodel=serviceModelId).filter(boolWorks="0").filter(endDate__gte=datetime.today())
    paginator = Paginator(articleList,FRONT_ARTICLES_NUMS)
    if not pageId:
        pageId = 1
    try:
        articles = paginator.page(pageId)
    except PageNotAnInteger: 
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(pageId)
    return render(request,'ajax/front-articles.html',{"articles":articles})

def serviceOutArticle(request,serviceModelId,pageId):
    outArticleList = Article.objects.filter(servicemodel=serviceModelId).filter(boolWorks="0").filter(endDate__lte=datetime.today())
    outPaginator = Paginator(outArticleList,FRONT_ARTICLES_NUMS)
    if not pageId:
        pageId = 1
    try:
        outArticles = outPaginator.page(pageId)
    except PageNotAnInteger: 
        outArticles = outPaginator.page(1)
    except EmptyPage:
        outArticles = outPaginator.page(outPaginator.num_pages)
    return render(request,'ajax/front-articles.html',{"articles":outArticles})

def classArticle(request,serviceModelId,classModelId,pageId):
    articleList = Article.objects.filter(servicemodel=serviceModelId).filter(classmodel=classModelId).filter(boolWorks="0").filter(endDate__gte=datetime.today())
    paginator = Paginator(articleList,FRONT_ARTICLES_NUMS)
    if not pageId:
        pageId = 1
    try:
        articles = paginator.page(pageId)
    except PageNotAnInteger: 
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(pageId)
    return render(request,'ajax/front-articles.html',{"articles":articles})

def classOutArticle(request,serviceModelId,classModelId,pageId):
    outArticleList = Article.objects.filter(servicemodel=serviceModelId).filter(classmodel=classModelId).filter(boolWorks="0").filter(endDate__lte=datetime.today())
    outPaginator = Paginator(outArticleList,FRONT_ARTICLES_NUMS)
    if not pageId:
        pageId = 1
    try:
        outArticles = outPaginator.page(pageId)
    except PageNotAnInteger: 
        outArticles = outPaginator.page(1)
    except EmptyPage:
        outArticles = outPaginator.page(pageId)
    return render(request,'ajax/front-articles.html',{"articles":outArticles})

def classModel(request,modelId):
    classModels = ClassModel.objects.filter(modelName=modelId)
    return render(request,'ajax/classModel.html',{"classModels":classModels})

def checkUserName(request,username):
    uname = username.strip()
    try:
        u = User.objects.get(username=uname)
    except Exception as e:
        return HttpResponse("0")
    else:
        return HttpResponse("1")

def page_not_found(request):
    return render(request,'dpub/404.html')

def page_error(request):
    return render(request,'dpub/503.html')
