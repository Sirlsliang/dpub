from django.conf.urls import url,include

from dpub.backend.views import *
from dpub.front.views import *


urlpatterns =[
    url(r'^$',Login.as_view(),name='userLogin'),
    url(r'^user/login/$',Login.as_view(),name='userLogin'),
    url(r'^user/logout/$',Logout.as_view(),name='userLogout'),
    url(r'^user/add/$',UserAdd.as_view(),name='userAdd'),
    url(r'^user/manage',UserManage.as_view(),name='userManage'),
    url(r'^user/password',changePassword,name="userPassword"),
    url(r'^manage/$',Manage.as_view(),name='backendManage'),
    url(r'^article/add/(?P<boolWorks>[0-1]+)/$',articleAdd),       
    url(r'^article/(?P<boolWorks>[0-1]+)/(?P<page>[0-9]+)/$',articlesManage,name='articlesManage'),
    url(r'^article/update/(?P<pk>[0-9]+)/$',articleUpdate,name="articleUpdate"),
    url(r'^article/del/(?P<pk>[0-9]+)/$',articleDel,name="articleDel"),
]

