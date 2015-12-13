#coding:utf-8#
import os,datetime
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

from dpub.models import *
from dpub.forms import * 

from dpub.conf import *
class LoginProtectedView(TemplateView): 
    @method_decorator(login_required(redirect_field_name='next',login_url='/manage/user/login'))
    def dispatch(self,*args,**kwargs):
        return super(LoginProtectedView,self).dispatch(*args,**kwargs)


class Login(View):
    def post(self,request):
        errorText = ""
        url = "/manage/user/login/"
        userName = request.POST['userName']
        password = request.POST['password']
        user = authenticate(username=userName,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                errorText = "恭喜你,登陆成功。"
                url = "/manage/manage/"
                return HttpResponseRedirect("/manage/manage/")
            else:
                errorText ="用户未激活,请联系客服人员！！！"
        else:
            errorText = "用户名或密码错误！!！"
        return render(request,'message.html',{'message':errorText,'url':url})

    def get(self,request):
        return render(request,'dpub/signup.html')

class Logout(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect('/')
def changePassword(request):
    if request.method =="POST":
        url = "/manage/manage/"
        errorText =""
        password = request.POST['password']
        newpassword = request.POST['newpassword']
        connewpassword = request.POST['connewpassword']
        if authenticate(username=request.user.username,password=password):
            user = request.user
            if newpassword and  newpassword == connewpassword:
                user.set_password(newpassword)
                user.save()
                logout(request)
                errorText = "密码修改成功"
            else:
                errorText = "两次密码输入不一致"
        else:
            errorText = "原始密码输入错误"
        return render(request,'message.html',{"message":errorText,"url":url})        

class UserManage(LoginProtectedView):
    def get(self,request):
        return render(request,"dpub/user-modify.html",{'user':request.user})

    def post(self,request):
        errorText =""
        url = "/manage/user/add/"
        user = request.user
        exUserForm = ExUserForm(request.POST)
        try:
            if exUserForm.is_valid():
                if exUserForm.cleaned_data['nickname']:
                    user.exuser.nickname = exUserForm.cleaned_data['nickname']
                if request.POST['sex']:
                    user.exuser.sex = request.POST['sex']
                if exUserForm.cleaned_data['phonenum']:
                    user.exuser.phonenum = exUserForm.cleaned_data['phonenum']
                if exUserForm.cleaned_data['companyname']:
                    user.exuser.companyname = exUserForm.cleaned_data['companyname']
            if request.POST['email']:
                user.email = request.POST['email']
            if request.POST['username']:
                user.username = request.POST['username']
            user.exuser.save()
            user.save()
            errorText = "修改成功"
        except Exception as e:
            errorText ="出错啦".joined(e)
        return render(request,'message.html',{'message':'修改成功','url':'/manage/manage/'})
        

class UserAdd(View):
    def post(self,request):
        errorText =""
        url = "/manage/user/add/"
        conpassword = request.POST['conpassword']
        exUserForm = ExUserForm(request.POST)
        userForm = UserForm(request.POST)
        if exUserForm.is_valid() and userForm.is_valid():
            if conpassword == userForm.cleaned_data['password']:
                try:
                    username = userForm.cleaned_data['username']
                    password = userForm.cleaned_data['password']
                    email = userForm.cleaned_data['email']
                    user = User.objects.create_user(username,email,password)
                    customer = Group.objects.get(name='customer')
                    user.groups.add(customer)
                    exUser = exUserForm.save(commit=False)
                    exUser.user = user
                    exUser.save()
                    user.save()
                    errorText = "注册成功"
                    url = "/manage/user/login/"
                except Exception as e:
                    errorText = e
            else:
                errorText ="两次输入密码不一致"
        else:
            errorText = exUserForm.errors.join(userForm.errors)
        return render(request,'message.html',{'message':errorText,'url':url})

    def get(self,request):
        return render(request,'dpub/register.html')

class Manage(LoginProtectedView):
    def get(self,request):
        allServiceModel = ServiceModel.objects.all()
        return render(request,'dpub/manage.html',{'allServiceModel':allServiceModel,})


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
            return render(request,'message.html',{'message':'添加成功','url':'/manage/manage/'})
        return render(request,'message.html',{'message':'访问出错'.join(articleForm.errors),'url':'/manage/manage/'})

@login_required(redirect_field_name='next',login_url='/manage/user/login')
def articlesManage(request,page):
    user = request.user
    articleList = Article.objects.filter(user=user)
    paginator = Paginator(articleList,ARTICLE_NUMS)
    if not page:
        page = 1
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1) 
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request,'ajax/article.html',{'articles':articles})

@login_required(redirect_field_name='next',login_url='/manage/user/login')
def articleUpdate(request,pk):
    if request.method == "GET":
        article = Article.objects.get(pk=pk)
        articleForm = ArticleForm(instance=article)
        return render(request,'dpub/article.html',{'article':articleForm })
    else:
        return HttpResponse("POST")


@login_required(redirect_field_name='next',login_url='/manage/user/login')
def articleDel(request,pk):
    Article.objects.get(pk=pk).delete()
    articleList = Article.objects.filter(user=request.user)
    paginator = Paginator(articleList,ARTICLE_NUMS)
    articles = paginator.page(1)
    return render(request,'ajax/article.html',{'articles':articles})

