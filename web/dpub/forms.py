#coding:utf-8#
from django import forms
from django.contrib.auth.models import User
from .models import *
class UserForm(forms.Form):
    IDENTICAL = (
        ('1','企业'),
        ('0','学生'),
    )
    userName = forms.CharField(label='用户名',max_length=99,error_messages={'required':'请输入用户'})
    password = forms.CharField(label='密码',max_length=100)
    conPassword = forms.CharField(label='确认密码',max_length=100)
    email = forms.EmailField()
    identity = forms.ChoiceField(label='身份',choices=IDENTICAL)
