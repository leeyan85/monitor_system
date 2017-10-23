"""SCMDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView

''''
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',  'devself.views.login2'),
    url(r'^accounts/login/$',  'devself.views.login2'),
    url(r'^accounts/login2/$',  'devself.views.login2'),
    url(r'^home/$','devself.views.home'),
    url(r'^modifypassword/(.+)/$','devself.views.ModifyVmPassword'),
    url(r'^restartvnc/(.+)/$','devself.views.restartvnc'),
    url(r'^mountnfs/(.+)/$','devself.views.mountnfs'),
    url(r'^logout/$','devself.views.logout'),    
]
'''
urlpatterns = patterns('',
    url(r'^admin/', admin.site.urls),
    url(r'^webapp/devself/', include('devself.urls')),
    #url(r'^release_notes/', include('release_notes.urls',namespace='release_notes')),
)
