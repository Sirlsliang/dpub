#coding:utf-8

from django.core.exceptions import ValidationError

def vald_phonenum(value):
    if (len(value)<11):
        raise ValidationError('电话号码长度不足11位') 


