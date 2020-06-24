from django.shortcuts import render

# Create your views here.
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth.models import User


def index(request):
  paginate_by = 3

  entry =Post.objects.order_by('created_on').values_list('title','slug','author','updated_on','content','created_on','status','postid')
    
  post = list(entry)
  #post = 30*post
  paginator = Paginator(post, 4) # Show 10 posts per page.
  page = request.GET.get('page')
  post = paginator.get_page(page)


  context = {'post':post,}

  return render(request, 'index.html',context)



def readmore(request,postid):
  if request.method == 'POST':
    comment_text = request.POST['comment_text']
    username=request.user.username
    postid = request.POST['postid']
    objComment = Comment(comment_text=comment_text, username=username,postid=postid)
    objComment.save()
  

  comments =Comment.objects.values_list('username','created_on','comment_text','postid',).filter(postid=postid)    
  comments = list(comments)
  noofcomments = len(comments)


  entry =Post.objects.order_by('created_on').values_list('title','slug','author','updated_on','content','created_on','status','postid',).filter(postid=postid)    
  post = list(entry)

  context = {'post':post,
  'comments':comments,
  'noofcomments':noofcomments}
  return render(request,'post_detail.html',context)