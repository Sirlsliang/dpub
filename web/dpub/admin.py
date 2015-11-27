from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(User)


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

