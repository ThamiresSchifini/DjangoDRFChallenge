"""ApiemDjangoNavarra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
<<<<<<< HEAD
from django.urls import path
from ApiemDjangoNavarra.files.views import files, remote

urlpatterns = [
    path('admin/', admin.site.urls),
    path('resources/files/', files),
    path('resources/remote/', remote )
=======
from django.urls import path, include
from django.http import HttpResponse
from ApiemDjangoNavarra.files.views import files
#from ApiemDjangoNavarra.files.views import FileHistoryViewsSet
from rest_framework import routers

#router = routers.DefaultRouter()
#router.register(r'files', files)

urlpatterns = [
    #path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('files/', files)
>>>>>>> 01611cbef7d7db9c0e4f50dde6af17589b0f2e92
]
