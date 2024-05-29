#This file we list our blog app-specific URLs
from . import views
from django.urls import path

#elow the imports, add a urlpattern for your PostList class-based view named home.
#As the view is a class, you need an as_view() method, unlike the previous function-based view.

urlpatterns = [
    path('', views.PostList.as_view(), name='home')
]