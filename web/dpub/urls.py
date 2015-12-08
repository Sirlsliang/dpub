from django.conf.urls import url,include

from dpub.views import *
backendurlpatterns=[
    url(r'^user/login/$',Login.as_view(),name='userLogin'),
    url(r'^user/logout/$',Logout.as_view(),name='userLogout'),
    url(r'^user/add/$',UserAdd.as_view(),name='userAdd'),
    url(r'^user/manage',UserManage.as_view(),name='userManage'),
    url(r'^manage/$',Manage.as_view(),name='backendManage'),
    url(r'^article/add$',ArticleAdd.as_view(),name='articleAdd')        
]


urlpatterns =[
    url(r'^$',Login.as_view(),name='userLogin'),
    url(r'^backend/',include(backendurlpatterns))
   ]
