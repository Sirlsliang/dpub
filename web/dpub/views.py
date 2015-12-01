from django.shortcuts import render
from django.shortcuts import render_to_response

from django.views.generic import View

from .models import *
from .forms import * 

# Create your views here.
class IndexView(View):
    def get(self,request):
        form = UserForm()
        allServiceModel = ServiceModel.objects.all()
        return render(request,'dpub/index.html',{'allServiceModel':allServiceModel,'form':form})

class Login(View):
    def get(self,request):
        form=UserForm()
        return render(request,'dpub/register.html',{'form':form})
