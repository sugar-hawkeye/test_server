"""test_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls.static import static
from test_server.settings import common,dev
from django.conf.urls import  include
from rest_framework.documentation import include_docs_urls

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Test API')

urlpatterns = [
    path(r'admin/', admin.site.urls),
    # re_path(r'^schema/$', schema_view),
    # re_path(r'^docs/', include_docs_urls(title='API DOC')),
    re_path(r'^',include('test_server.apps.tag.urls')),
    re_path(r'^api-auth/', include('rest_framework.urls')),
]

if dev.DEBUG:
    import debug_toolbar
    urlpatterns.append(path(r'^__debug__/', include(debug_toolbar.urls)))

urlpatterns += static(common.STATIC_URL, document_root=common.STATIC_ROOT)




#1.request
#2.response
#3.serializer
#4.permission
#5.authentication
#6.relationship
#7.viewset
#8.router
#9.settings