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
    @method_decorator(login_required(redirect_field_name='next',login_url='/manage/user/login/'))
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
	exUserForm = ExUserForm(instance=request.user.exuser)
    	allServiceModel = ServiceModel.objects.all()
        return render(request,"dpub/user-modify.html",{'exUserForm':exUserForm,'user':request.user,'allServiceModel':allServiceModel})

    def post(self,request):
        errorText =""
        url = "/manage/user/add/"
        user = request.user
	exUserForm = ExUserForm(request.POST)
        allServiceModel = ServiceModel.objects.all()
        if exUserForm.is_valid():
            exUser = exUserForm.save(commit=False)
            exUser.id = user.exuser.id
            user.exuser = exUser
            if request.POST['email']:
                user.email = request.POST['email'].strip()
            if request.POST['username']:
                user.username = request.POST['username'].strip()
            user.exuser.save()
            user.save()
        else:
            return render(request,"dpub/user-modify.html",{'exUserForm':exUserForm,'user':request.user,'allServiceModel':allServiceModel})
        return render(request,'message.html',{'message':'修改成功','url':'/manage/manage/'})
        

class UserAdd(View):
    def post(self,request):
        errorText =""
        url = "/manage/user/add/"
        userForm =MyUserForm(request.POST)
        if userForm.is_valid():
            password = userForm.cleaned_data['password']
            conpassword = userForm.cleaned_data['conpassword']
            if password == conpassword:
                try:
                    username = userForm.cleaned_data['username']
                    email = userForm.cleaned_data['email']
                    user = User.objects.create_user(username,email,password)
                    customer = Group.objects.get(name='customer')
                    user.groups.add(customer)
		    sex = userForm.cleaned_data['sex']
		    phonenum = userForm.cleaned_data['phonenum']
		    companyname = userForm.cleaned_data['companyname']
                    exUser= Exuser(user=user,sex=sex,phonenum=phonenum,companyname=companyname)
                    exUser.save()
                    user.save()
                    errorText = " 恭喜您，注册成功"
		    url = "/"
                except Exception as e:
                    errorText = e
            else:
                errorText ="两次密码输入不一致"
            return render(request,'message.html',{'message':errorText,'url':url})
        else:
            return render(request,'dpub/register.html',{'userForm':userForm,'url':url})

    def get(self,request):
        userForm    =   MyUserForm()
        return render(request,'dpub/register.html',{'userForm':userForm})

class Manage(LoginProtectedView):
    def get(self,request):
        allServiceModel = ServiceModel.objects.all()
        return render(request,'dpub/manage.html',{'allServiceModel':allServiceModel,})

def articleAdd(request,boolWorks): 
	var = None
	if boolWorks == '0':
		var = '需求'
	elif boolWorks == '1':
		var = '作品'
	allServiceModel = ServiceModel.objects.all()
	if request.method == "GET":
		articleForm = ArticleForm()
		return render(request,'dpub/release.html',{'var':var,'articleForm':articleForm,'allServiceModel':allServiceModel,'boolWorks':boolWorks})
	
	if request.method == "POST":
		user = request.user
		articleForm = ArticleForm(request.POST,request.FILES)
		if articleForm.is_valid():
			article = articleForm.save(commit=False)
			if not article.usernickname:
				article.usernickname = user.exuser.nickname
			if not article.phonenum:
				article.phonenum = user.exuser.phonenum
			if not article.email:
				article.email = user.email
			if not article.companyname:
				article.companyname = user.exuser.companyname
			article.user = request.user
			article.save()
			return HttpResponseRedirect('/manage/manage/')
		else:
			return render(request,'dpub/release.html',{'articleForm':articleForm,'allServiceModel':allServiceModel,'var':var,'boolWorks':boolWorks})

@login_required(redirect_field_name='next',login_url='/manage/user/login')
def articlesManage(request,boolWorks,page):
    user = request.user
    articleList = Article.objects.filter(user=user).filter(boolWorks=boolWorks)
    paginator = Paginator(articleList,ARTICLE_NUMS)
    if not page:
        page = 1
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1) 
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request,'ajax/article.html',{'articles':articles,'boolWorks':boolWorks})


@login_required(redirect_field_name='next',login_url='/manage/user/login')
def articleUpdate(request,pk):
	article = Article.objects.get(pk=pk)
	boolWorks = article.boolWorks
	var = None
	if boolWorks == '0':
		var = "需求"
	elif boolWorks == '1':
		var = "作品"
	allServiceModel = ServiceModel.objects.all()
	if request.method == "GET":
		articleForm = ArticleForm(instance=article)
		return render(request,'dpub/release-modify.html',{'allServiceModel':allServiceModel,'pk':pk,'articleForm':articleForm,'boolWorks':boolWorks,'var':var})
	
	if request.method == "POST":
		user = request.user
		articleForm = ArticleForm(request.POST,request.FILES)
		if articleForm.is_valid():
			art = articleForm.save(commit=False)
			article.title   = art.title
			article.content = art.content
			article.servicemodel = art.servicemodel
			article.classmodel   = art.classmodel
			if art.img:
				article.img	     = art.img
			if article.boolWorks == '0':
				article.endDate = art.endDate
			article.price = art.price
			article.companyname = art.companyname
			article.usernickname = art.usernickname
			article.email = art.email
			article.phonenum = art.phonenum
			article.save()
			return render(request,'message.html',{'message':'修改成功','url':'/manage/manage/'})
		return render(request,'dpub/release-modify.html',{'allServiceModel':allServiceModel,'pk':pk,"articleForm":articleForm,'boolWorks':boolWorks,'var':var})

@login_required(redirect_field_name='next',login_url='/manage/user/login')
def articleDel(request,pk):
    Article.objects.get(pk=pk).delete()
    articleList = Article.objects.filter(user=request.user)
    paginator = Paginator(articleList,ARTICLE_NUMS)
    articles = paginator.page(1)
    return render(request,'ajax/article.html',{'articles':articles})

