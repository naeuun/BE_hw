from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    path('', main, name='main'),
    path('detail/<int:id>/', detail, name='detail'),
    path('create-comment/<int:id>', create_comment, name='create-comment'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
    path('delete-comment/<int:id>', delete_comment, name='delete-comment'),
    path('category/<slug:slug>/', category, name='category'),
    path('like/<int:post_id>/', like, name='like'),
    path('scrap/<int:post_id>/', scrap, name='scrap'),
]
