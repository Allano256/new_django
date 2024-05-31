"""
URL configuration for codestar project.

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
from django.urls import path, include
#from blog import views as index_views ...We delete this after creating a url.py file in 
#the blog folder because now the blog has its own url file

#Ensure that include is imported from django.urls by appending it after path.

urlpatterns = [
    #path('blog/', index_views.index, name= 'index'), We also replace this after creating a url.py file in 
#the blog folder, Also, replace the existing blog/ urlpattern with a new empty string urlpattern.
    #This pattern tells Django to look in the blog app URL file for any blog urlpatterns.
        
    
      path("about/", include("about.urls"), name="about-urls"),

      path("accounts/", include("allauth.urls")),

      path('admin/', admin.site.urls),

      path('summernote/', include('django_summernote.urls')),
      
      path("", include("blog.urls"), name='blog-urls'), 

     
    #This is what we work with after working on models and creating views
   
]


#Next, we need to create a templates directory in the blog app, with another directory nested within, 
# named blog. Django expects this file structure. To create the directory structure, 
# use the following command in the terminal:

#mkdir -p blog/templates/blog
