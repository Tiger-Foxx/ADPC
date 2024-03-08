"""
URL configuration for ADPC project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from ADPC import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from ADPC_APP.views import *
urlpatterns = [
    path('',index,name='index'),
    path('admin/', admin.site.urls),
    path('post/<str:id>/', post_detail,name='post'),
    path('postTag/<str:tag>/', post_Tag,name='postTag'),
    path('blog/<str:tag>/', blogTag,name='blogTag'),
    path('blog/', blog,name='blog'),
    path('adhesion/', adhesion,name='adhesion'), # type: ignore
    path('Don/', don,name='don'), # type: ignore
    path('Volontariat/', volontariat,name='Volontariat'), # type: ignore

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
