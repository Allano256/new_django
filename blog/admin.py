from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


#This code will give your admin panel greater functionality and clarity.
#Note: The decorator is how we register a class, 
# compared to just registering the standard model as we did before. 
# When we use a class, we register it with a decorator that is more Pythonic and allows us
#  to customise how the models we are registering will appear on the admin site.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title',]
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

#he dot in front of models on line 2 indicates that we are importing Post from a file named models, which is in the same directory as our admin.py file.
#  If you have multiple models that you want to import, then you can separate them with a comma

# Register your models here.
#This will allow you to create, 
#update and delete blog posts from the admin panel.
# However, please refrain from adding any posts at the moment, 
# #as there are more fields to be added to the tables in an upcoming topic.


#When we create a custom model and we want it to appear in the admin site, then we need to tell Django by registering it in the admin.py file.
#  That is what admin.site.register does.
#It is worth noting that the admin.site.register method takes only one argument. If you are registering multiple models,
#  you would need a separate line for each model

#admin.site.register(Post)  #This is deleted after registering the Post with a decorator
admin.site.register(Comment)

#admin.site.register(Comment)