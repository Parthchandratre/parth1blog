from django.db import models

# Create your models here.
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
   postid = models.IntegerField(blank=True,null =True)
   title = models.CharField(max_length=200, unique=True)
   slug = models.SlugField(max_length=200, unique=True)
   author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
   updated_on = models.DateTimeField(auto_now= True)
   content = models.TextField()
   created_on = models.DateTimeField(auto_now_add=True)
   status = models.IntegerField(choices=STATUS, default=0)

   class Meta:
       ordering = ['-created_on']

   def __str__(self):
       return self.title


class Comment(models.Model):
   postid = models.IntegerField(blank=True,null =True)
   comment_text = models.TextField()
   username = models.CharField(max_length=50)
   created_on = models.DateTimeField(auto_now_add=True)

 
   def __str__(self):
       return self.username