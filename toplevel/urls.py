"""
URL configuration for toplevel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from bottomlevel.views import index,deletetask,edittask,contact,login_view,registration,logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index,name='index'),
    path('delete/<str:id>',deletetask,name='delete-task'),
    path('edit/<str:id>',edittask,name='edit-task'),
    path('contact',contact,name='contact'),
    path('login',login_view,name='login'),
    path('registration',registration,name='registration'),
    path('logout_view',logout_view,name='logout_view')

]
