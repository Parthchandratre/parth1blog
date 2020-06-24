from django.contrib import admin

# Register your models here.
from .models import * 

class PostAdmin(admin.ModelAdmin):
    list_display = ('postid','title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
  
admin.site.register(Post, PostAdmin)




class CommentAdmin(admin.ModelAdmin):
    list_display = ('username','postid','comment_text', 'created_on',)
   
  
admin.site.register(Comment, CommentAdmin)