from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from webapp.models import Article


# Create your views here.
def index(request):
    articles = Article.objects.order_by('-created_at')
    return render(request, 'index.html', {"articles": articles})


def create_article(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        article = Article.objects.create(title=title, content=content, author=author)
        return redirect('index',pk=article.pk)
    else:
        return render(request, 'create_article.html')


def article_detail(request,*args,**kwargs):
    article_id = kwargs.get('pk')
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'detail_article.html', {"article": article})