"""hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static



#路由入口文件

urlpatterns = [  #主路由表

    path('admin/', admin.site.urls),

   # path('api/mgr/',include('mgr.urls')),


    # path('register/',register),
    path('login/',include('login.urls')),
    path('patient/',include('patient.urls')),
    path('doctor/', include('doctor.urls')),
    path('manager/',include('manager.urls')),
    path('medicine/',include('medicine.urls')),

]+  static("/", document_root="./templates")
