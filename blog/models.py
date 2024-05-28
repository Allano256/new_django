from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
#So here the Post is inheriting from Model class
#The title values should be unique to avoid having blog posts of the same name confusing your users.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug= models.SlugField(max_length=200, unique=True)#In publishing, a slug is a short name for an article that is still in production
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")#One user can write many posts, so this is a one to many or foreign key
    content = models.TextField() #This is the blog article content
    created_on = models.DateTimeField(auto_now_add = True) #The auto_now_add= True, means the default created time is the time of post entry.
    status = models.IntegerField(choices=STATUS, default=0) #A draft is defined as zero and published as one, so you can see the default is to save as a draft.

