from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
#So here the Post is inheriting from Model class
#The title values should be unique to avoid having blog posts of the same name confusing your users.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug= models.SlugField(max_length=200, unique=True)#In publishing, a slug is a short name for an article that is still in production
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")#One user can write many posts, so this is a one to many or foreign key,
                                                                                     #models.CASCADE: if a user is deleted, then any posts they have authored will also be deleted.
    content = models.TextField() #This is the blog article content
    created_on = models.DateTimeField(auto_now_add = True) #The auto_now_add= True, means the default created time is the time of post entry.
    status = models.IntegerField(choices=STATUS, default=0) #A draft is defined as zero and published as one, so you can see the default is to save as a draft.
    exerpt = models.TextField(blank=True)#As the excerpt is optional, the user must be able to leave
    # this database row blank without throwing an error. The Excerpt is a summary or teaser visible on the main page. 
    # Choose wording that would make a user want to click and read more.
    updated_on = models.DateTimeField(auto_now=True) #The auto_now argument for the updated_on field sets the value to the current date and time whenever the record is saved,
    #not just when it is created.


class Comment(models.Model):
    post =  models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")#If a blog post is deleted the comments 
    #on it should also be deleted. Should have a many-to-one relationship with the Post model.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")#If a user account is deleted the user's 
    #comments will be deleted also.Should have a many-to-one relationship with the built-in User model.
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add = True)
   


