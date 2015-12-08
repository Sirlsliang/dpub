#coding:utf-8#
import os
from django.conf import settings
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect

from django.views.generic import View,ListView
from django.views.generic import TemplateView

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,Group

from django.contrib.auth.decorators import login_required,permission_required
from django.utils.decorators import method_decorator

from .models import *
from .forms import * 

class LoginProtectedView(TemplateView): 
    @method_decorator(login_required(redirect_field_name='next',login_url='/manage/backend/user/login'))
    def dispatch(self,*args,**kwargs):
        return super(LoginProtectedView,self).dispatch(*args,**kwargs)

# Create your views here.
class IndexView(View):
    def get(self,request):
        allServiceModel = ServiceModel.objects.all()
        return render(request,'dpub/index.html',{'allServiceModel':allServiceModel,})

class Login(View):
    def post(self,request):
        userName = request.POST['userName']
        password = request.POST['password']
        user = authenticate(username=userName,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect("/manage/backend/manage/")
            else:
                return HttpResponse("user is not active")
        else:
            return HttpResponse("user is none")

    def get(self,request):
        return render(request,'dpub/signup.html')

class Logout(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect('/')

class UserManage(LoginProtectedView):
    def get(self,request):
        return HttpResponse("用户管理")

class UserAdd(View):
    def post(self,request): 
        username = request.POST['username'] 
        password = request.POST['password']
        email    = request.POST['email']
        conpassword = request.POST['conPassword']
        identity = request.POST['identity']
        try:
            if password and conPassword and password == conpassword:
                user = User.objects.create_user(username,email,password)
                exuser= Exuser(user=user,identity=identity)
                exuser.save()
                customer = Group.objects.get(name='customer')
                user.groups.add(customer)
                user.save()
                return HttpResponseRedirect("admin")
        except Exception as e:
            return HttpResponse("添加用户异常:%s"%e)

    def get(self,request):
        userForm = UserForm()
        return render(request,'dpub/register.html',{'userForm':userForm})

class Manage(LoginProtectedView):
    def get(self,request):
        allServiceModel = ServiceModel.objects.all()
        user = request.user
        articleList = Article.objects.filter(user=user)
        paginator = Paginator(articleList,3)
        page = request.GET['page']
        if not page:
            page = 1
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1) 
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)

        return render(request,'dpub/manage.html',{'allServiceModel':allServiceModel,'articles':articles})


class ArticleAdd(LoginProtectedView): 

    def get(self,request):
        allServiceModel = ServiceModel.objects.all()
        articleForm = ArticleForm()
        return render(request,'dpub/release.html',{'allServiceModel':allServiceModel,'articleForm':articleForm,})
    def post(self,request):
        articleForm = ArticleForm(request.POST,request.FILES)
        if articleForm.is_valid():
            article = articleForm.save(commit=False)
            article.user = request.user
            article.save()
            return HttpResponse("%s , %s, %s, %s, %s, %s"%(article.title,article.content,article.img,article.phonenum,article.endDate,article.email))
        return HttpResponse("Wrong")


















