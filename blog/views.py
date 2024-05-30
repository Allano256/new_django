from django.shortcuts import render, get_object_or_404
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

    queryset = Post.objects.filter(status=1) #he queryset applies a filter on the
    #database to get only posts with a status of 1, which,
    #from the STATUS constant in models.py, we know is mapped to "Published".
    #template_name = "post_list.html"

    template_name = "blog/index.html"
    paginate_by = 6

   # model = Post...We can remove the model = Post as it is made redundant by the queryset 
   # explicitly stating all posts are displayed.

def post_detail(request, slug):
    """
    The slug parameter gets the argument value from the URL pattern named post_detail.

    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
        
    )