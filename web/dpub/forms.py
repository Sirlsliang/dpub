#coding:utf-8#
from django.forms import ModelForm,PasswordInput,forms

from django.contrib.auth.models import User
from .models import *

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude =['date_joined']

class ExUserForm(ModelForm):
    class Meta:
        model = Exuser
        fields = '__all__'
        exclude =['user']


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields ='__all__'
        exclude =['user']
