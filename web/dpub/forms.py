#coding:utf-8#
from django import forms
from django.forms import ModelForm,PasswordInput

from django.contrib.auth.models import User
from .models import *

class UserForm(ModelForm):
    class Meta:
        model  = User
        fields = ['username','password','email']

class ExUserForm(ModelForm):
	class Meta:
		model = Exuser
		fields = '__all__'   
		exclude =['user','headimg','server','boolServer']
		widgets={
			'nickname':forms.TextInput(attrs={'class':'input'}),
			'phonenum':forms.TextInput(attrs={'class':'input','minlength':'7','maxlength':'16','required':'','pattern':r'^\d{8,15}$'}),
			'companyname':forms.TextInput(attrs={'class':'input','required':True}),
			'sex':forms.Select(attrs={'class':'input'})
		}
	
class MyUserForm(forms.Form):
    SEX_CHOICES = (
        ('0','男'),
        ('1','女')
    )
    username = forms.CharField(max_length=30,label="帐号",widget=forms.TextInput(attrs={'minlength':'3','placeholder':'输入用户名（至少三个字符)','required':'','pattern':r'\w{3,30}','onblur':'checkTheUserName(id_username)'}))
    
    password = forms.CharField(max_length=100,label="密码",widget=forms.TextInput(attrs={'type':'password','placeholder':'请输入六位以上的数字字符组合','pattern':r'^\w{6,}$','data-foolish-msg':'请填写密码','required':''}))
    conpassword = forms.CharField(max_length=100,label="确认密码",widget=forms.TextInput(attrs={'type':'password','placeholder':'请重复上面的密码','pattern':r'^\w{6,}$','required':'','onblur':'checkPassword(id_password,id_conpassword)',r'data-equal-to':r'#password'}))
    email = forms.EmailField(label="邮箱" ,widget=forms.TextInput(attrs={'placeholder':'请输入邮箱','required':''}))
    sex = forms.CharField(widget=forms.Select(choices=SEX_CHOICES),label="性别")
    phonenum = forms.CharField(max_length=15,label="电话号码",widget=forms.TextInput(attrs={'placeholder':'请输入您的电话号码(8到15位)','minlength':'7','maxlength':'16','required':'','pattern':r'^\d{8,15}$'}))
    companyname = forms.CharField(max_length=100,label="单位名称",widget=(forms.TextInput(attrs={'placeholder':'请输入您的单位名称','required':''})))


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields ='__all__'
        widgets={
            'title':forms.TextInput(attrs={'class':'input','id':'sim-describe','required':True,'placeholder':'必填'}),
            'servicemodel':forms.Select(attrs={'id':r'category-selected','onchange':r'getTheClassModel()',r'data-am-selected':'','required':True}),
            'classmodel':forms.Select(attrs={'id':'classSelect',r'data-am-selected':'','class':r'sub-category','placeholder':'详细类别','required':True}),
            
            'endDate':forms.TextInput(attrs={'class':'input',r'data-am-datepicker':'','placeholder':'必填','required':True}),
            'price':forms.TextInput(attrs={'class':'input','pattern':r'^\d+$','placeholder':"必填",'required':True}),
            'usernickname':forms.TextInput(attrs={'class':'input','placeholder':'选填'}),
            'companyname':forms.TextInput(attrs={'class':'input','placeholder':'选填'}),
            'phonenum':forms.TextInput(attrs={'class':'input','placeholder':'选填'}),
            'email':forms.TextInput(attrs={'class':'input','placeholder':'选填'}),
        }
        exclude =['user','boolWorks']
