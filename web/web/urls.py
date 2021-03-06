"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from dpub.front.views import IndexView

urlpatterns = [
    #url(r'^',include('dpub.urls')),
    url(r'^$',IndexView.as_view(),name='Index'),
    url(r'^index.html$',IndexView.as_view(),name='Index'),
    url(r'^manage/',include('dpub.backend.urls')),
    url(r'^get/',include('dpub.front.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

handler404 = 'dpub.front.views.page_not_found'
handler500 = 'dpub.front.views.page_error'
