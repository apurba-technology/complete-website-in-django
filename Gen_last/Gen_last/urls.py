"""Gen_last URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from pro_last import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index), 
  
    path('banner_upload', views.banner_upload, name='banner_upload'), 
    path('notice_up', views.notice_upload),
    
    path('gallery_up',views.gallery_up),
    #########################################################
    path('admin', views.ind),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('reset', views.reset),
    path('wall', views.wall),
    ####################
    path('display_gallery',views.disg),
    path('display_banner',views.disb),
    path('display_notice',views.disn, name='display_notice'),
    path('contact',views.con, name='contact'),
    path('about',views.about, name='about'),
    path('delete_notice/<int:id>', views.delete_notice),
    path('delete_banner/<int:id>', views.delete_banner),
    path('delete_gallery/<int:id>', views.dele_gallery, name='delete_gallery'),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
