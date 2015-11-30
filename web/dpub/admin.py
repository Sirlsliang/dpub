from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import *
# Register your models here.

# show school information
class CourseInline(admin.StackedInline):
    model = Course
    extra = 3
class SchoolAdmin(admin.ModelAdmin):
    fieldsets = [
        ('SchoolName',{'fields':['schName']}),
        ('School Information',{'fields':['schDesc','schUrl','schLogo']})
    ]
    inlines = [CourseInline]
    list_display = ('schName',)
    search_fields = ['schName']
admin.site.register(School,SchoolAdmin)

#show service model
class ClassInline(admin.StackedInline):
    model = ClassModel
    extra = 3
class ServiceAdmin(admin.ModelAdmin):
    fieldsets =[
        ('ServiceModel',{'fields':['modelName','modelImg']}),        
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
admin.site.unregister(User)
admin.site.register(User,UserAdmin)
