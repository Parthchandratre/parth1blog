from django.urls import path,include,re_path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('readmore/<int:postid>/', views.readmore, name='readmore'),

    #path('category_main/', views.category_main, name="category_main"),
   


]



