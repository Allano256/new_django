from django.shortcuts import render
#from django.http import HttpResponse   #This you delete after creating the new html file in thye views

from django.views import generic
from .models import Post

# Create your views here.

#def index(request):
    #return HttpResponse("Helo, Blog!")  #This you delete after creating the new html file in thye views


# In the blog/views.py file, create a class-based view named PostList that inherits from the generic.
# ListView class to display all your posts.
class PostList(generic.ListView):
    #queryset = Post.objects.all() will return everything
    queryset = Post.objects.filter(status=1)
    #template_name = "post_list.html"
    template_name = "blog/index.html"
    paginate_by = 6

   # model = Post...We can remove the model = Post as it is made redundant by the queryset 
   # explicitly stating all posts are displayed.