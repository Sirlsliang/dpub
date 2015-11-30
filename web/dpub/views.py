from django.shortcuts import render
from django.shortcuts import render_to_response

from .models import *
from .form  import *

# Create your views here.
def Index(request):
    allServiceModel = ServiceModel.objects.all()
    return render(request,'dpub/index.html',{'allServiceModel':allServiceModel,})

def userLogin(request):
    form=UserForm()
    return render(request,'dpub/register.html',{'form':form})
