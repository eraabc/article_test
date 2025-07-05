from django.urls import path

from webapp.views import index, create_article, article_detail

urlpatterns = [
    path('', index,name='index'),
    path('add-article/', create_article, name='create_article'),
    path('article/<int:pk>/', article_detail, name='article_detail'),
]
