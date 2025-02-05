from django.contrib import admin
from .models import Post,Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_per_page=10
    list_display=['author','title','introduction','body','date_added']

@admin.register(Comment) 
class CommentAdmin(admin.ModelAdmin):
    list_per_page=10
    list_display=  [ 'user', 'post','name','email','body', 'date_added']
   
    
    
    
   
 
