from django.urls import path

from webapp.views import index, create_article, article_detail,update_article,delete_article

urlpatterns = [
    path('', index, name='index'),
    path('add-article/', create_article, name='add-article'),
    path('article/<slug:slug>/', article_detail, name='article-detail'),
    path('article/<int:pk>/update/', update_article, name='update-article'),
    path('article/<int:pk>/delete/', delete_article, name='delete-article'),
]
