from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='blogapp-home'),
    path('about/', views.about, name='blogapp-about'),
    path('<str:username>/', views.UserPostView.as_view(), name='users_blog'),
    path('post/<int:pk>/', views.PostDetails.as_view(), name='blog_post_detail'),
    path('post/create/', views.CreatePost.as_view(), name='blog-post-create'),
    path('post/<int:pk>/update', views.PostUpdate.as_view(), name='blog-post-update'),
    path('post/<int:pk>/delete', views.PostDelete.as_view(), name='blog-post-delete'),
    path('post/<int:pk>/comment/', views.add_comment, name='add_comments'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('comment/<int:pk>/edit/', views.comment_update, name='comment_edit'),
]

# views.home returns httpresponse object.
