#coding:utf-8#
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import *
# Register your models here.

# show school information

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 3

class ServersAdmin(admin.ModelAdmin):
    fieldsets = [
            ('服务商',{'fields':['servername','serverdesc','serverurl']}),
            ('详细信息',{'fields':['serverlogo','serverbanner','serverclass','servertel','serveraddress']})
    ]
    inlines = [LessonInline]
    list_display = ('servername',)
    search_fields = ['servername']
admin.site.register(Servers,ServersAdmin)



#show service model
class ClassInline(admin.StackedInline):
    model = ClassModel
    extra = 3

class ServiceAdmin(admin.ModelAdmin):
    fieldsets =[
        ('首页模块',{'fields':['modelName','modelImg']}),        
    ]
    inlines = [ClassInline]
    list_display = ('modelName',)
admin.site.register(ServiceModel,ServiceAdmin)

#show User model
class ExuserInline(admin.StackedInline):
    model = Exuser
    can_delete = False
    
class UserAdmin(UserAdmin):
    inlines = [ExuserInline,]

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','user','insertDate','endDate')
    search_fields = ['boolWorks']


admin.site.unregister(User)
admin.site.register(User,UserAdmin)


admin.site.register(Article,ArticleAdmin)








