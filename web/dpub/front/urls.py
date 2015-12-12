from django.conf.urls import url,include

from dpub.front.views import *
urlpatterns =[
    url(r"^servers/$",ServersView.as_view(),name="serversView"),
   ]
