from django.shortcuts import render, get_object_or_404, reverse
#from django.http import HttpResponse   #This you delete after creating the new html file in thye views

from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post,  Comment
from .forms import CommentForm

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
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

    

    def comment_delete(request, slug, comment_id):
         """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
    
    
   
