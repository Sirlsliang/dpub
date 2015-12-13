from django.conf.urls import url,include

from dpub.front.views import *
urlpatterns =[
    url(r"^servers/$",ServersView.as_view(),name="serversView"),
    url(r"^model/articles/(?P<serviceModelId>[0-9]+)/$",serviceArticle,name="serviceArticles"),
    url(r"^model/articles/(?P<serviceModelId>[0-9]+)/(?P<classModelId>[0-9]+)/$",classArticle,name="classArticles"),
    url(r"^article/article/(?P<articleId>[0-9]+)/$",articleDetail,name="articleArticle"),
   ]
