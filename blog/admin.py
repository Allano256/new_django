from django.contrib import admin
from .models import Post

# Register your models here.
#This will allow you to create, 
#update and delete blog posts from the admin panel.
# However, please refrain from adding any posts at the moment, 
# #as there are more fields to be added to the tables in an upcoming topic.
admin.site.register(Post)