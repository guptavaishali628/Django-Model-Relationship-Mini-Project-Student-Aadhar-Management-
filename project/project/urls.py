"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('add_aadhar/',add_aadhar, name='add_aadhar'),
    path('save_aadhar/',save_aadhar, name='save_aadhar'),
    path('add_student/',add_student, name='add_student'),
    path('save_student/', save_student, name="save_student"),
    path('show_aadhar/',show_aadhar, name='show_aadhar'),
    path('show_student/',show_student, name='show_student'),
    path('relation_table/',relation_table, name='relation_table'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
