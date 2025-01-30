from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('details/<int:id>/',views.details,name='details'),
    path('like-comment/<int:comment_id>/', views.like_comment, name='like_comment'),
    # path('like-reply/<int:reply_id>/', views.like_reply, name='like_reply'),
   
]