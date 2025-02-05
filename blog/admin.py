from django.contrib import admin
from .models import Post,Comment

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin): 
    list_per_page = 10
    list_display = ['author__username', 'author__email', 'title', 'introduction', 'body', 'date_added']
    list_filter = ['author__username', 'author__email', 'title', 'introduction', 'body', 'date_added']
    search_fields = ['author__username', 'author__email', 'title', 'introduction', 'body', 'date_added']
    list_display_links = ['author__username']
    list_editable = ['title']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['user__username', 'user__email', 'post', 'body', 'date_added']
    list_filter = ['user__username', 'user__email', 'post', 'body', 'date_added']
    search_fields = ['user__username', 'user__email', 'post', 'body', 'date_added']
    list_display_links = ['user__username']
    list_editable = ['post']
