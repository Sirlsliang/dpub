#coding:utf-8#
import os
from datetime import *
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

# Create your views here.
class IndexView(View):
    def get(self,request):
        allServiceModel = ServiceModel.objects.all()
        articles = Article.objects.order_by('boolIndex').filter(boolIndex__gte=0).filter(endDate__gte=datetime.today())
        return render(request,'dpub/index.html',{'allServiceModel':allServiceModel,'articles':articles,})


