"""textutil URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path
#from .import view
from .import view

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',templates.index,name='index')
    #path('',content.Navigator,name='Navigator')
    path('',view.index,name='index'),
    path('index2',view.index2,name='index2'),
    # path('removepunc',view.removepunc,name='removepunc'),
    # path('rcapitalizfirst',view.rcapitalizfirst,name='rcapitalizfirst'),
    # path('newlineremover',view.newlineremover,name='newlineremover'),
    # path('charcount',view.charcount,name='charcount'),
    path('Analyze',view.Analyze, name='Analyze'),
    
]
