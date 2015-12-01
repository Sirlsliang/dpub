from django.conf.urls import url

from dpub.views import *

urlpatterns =[
    #url(r'$/',views.get_index,name='index'),
    url(r'^login/$',Login.as_view(),name='userLogin')
]
