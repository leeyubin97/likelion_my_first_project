from django.contrib import admin
from django.urls import path
import blog.views


urlpatterns = [
    path('home', blog.views.home, name='home'),
    path('post/<int:post_id>/', blog.views.detail, name='detail'),
    path('post/new/', blog.views.post_new, name='new'),
    path('post/<int:post_id>/edit', blog.views.post_edit, name='edit'),
    path('post/<int:post_id>/delete', blog.views.post_delete, name='delete'),
    path('post/<int:post_id>/comment', blog.views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/delete', blog.views.comment_delete, name="comment_delete"),
]
