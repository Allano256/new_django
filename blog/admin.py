from django.contrib import admin
from .models import Post #,comment
#he dot in front of models on line 2 indicates that we are importing Post from a file named models, which is in the same directory as our admin.py file.
#  If you have multiple models that you want to import, then you can separate them with a comma

# Register your models here.
#This will allow you to create, 
#update and delete blog posts from the admin panel.
# However, please refrain from adding any posts at the moment, 
# #as there are more fields to be added to the tables in an upcoming topic.


#When we create a custom model and we want it to appear in the admin site, then we need to tell Django by registering it in the admin.py file. That is what admin.site.register does.
#It is worth noting that the admin.site.register method takes only one argument. If you are registering multiple models, you would need a separate line for each model
admin.site.register(Post)
#admin.site.register(Comment)