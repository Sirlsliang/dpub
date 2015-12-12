from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.views.generic import View

from django.contrib.auth import authenticate,login

from django.contrib.auth.models import User
from .models import *
from .forms import * 

# Create your views here.
class IndexView(View):
    def get(self,request):
        form = UserForm()
        allServiceModel = ServiceModel.objects.all()
        return render(request,'dpub/index.html',{'allServiceModel':allServiceModel,'form':form})

class Login(View):
    def post(self,request):
        userName = request.POST['userName']
        password = request.POST['password']
        user = authenticate(username=userName,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponse("success")
            else:
                return HttpResponse("user is not active")
        else:
            return HttpResponse("user is none")

class UserAdd(View):
    def post(self,request):
        userName = request.POST['userName']
        email = request.POST['email']
        pwd  = request.POST['password']
        conpwd = request.POST['conPassword']
        identity = request.POST['identity']
        
        user =User.objects.create_user(userName,email,pwd)
        exuser = Exuser.objects.create(user=user,identity=identity)
        exuser.save()
        user.save()
        return HttpResponseRedirect('/admin')

























