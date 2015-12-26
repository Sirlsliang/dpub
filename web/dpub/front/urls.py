from django.conf.urls import url,include

from dpub.front.views import *
urlpatterns =[
    url(r"^servers/$",ServersView.as_view(),name="serversView"),
    url(r"^server/(?P<pk>[0-9]+)/$",server),
    url(r"^contactus",ContactUsView.as_view(),name="contactUsView"),
    url(r"^classmodel/(?P<modelId>[0-9]+)/$",classModel),

    url(r"^servicemodel/(?P<serviceModelId>[0-9]+)/$",serviceModelArticles),
    url(r"^servicemodel/(?P<serviceModelId>[0-9]+)/classmodel/(?P<classModelId>[0-9]+)/$",classModelArticles),

    url(r"^articles/(?P<serviceModelId>[0-9]+)/(?P<pageId>[0-9]+)/$",serviceArticle),
    url(r"^articles/(?P<serviceModelId>[0-9]+)/(?P<classModelId>[0-9]+)/(?P<pageId>[0-9]+)/$",classArticle),

    url(r"^outarticles/(?P<serviceModelId>[0-9]+)/(?P<pageId>[0-9]+)/$",serviceOutArticle),
    url(r"^outarticles/(?P<serviceModelId>[0-9]+)/(?P<classModelId>[0-9]+)/(?P<pageId>[0-9]+)/$",classOutArticle),

    url(r"^article/(?P<articleId>[0-9]+)/$",articleDetail),

   ]
