from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404

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
        # return HttpResponseRedirect("/")
        return redirect("article-detail", pk=article.pk)
    else:
        return render(request, 'create_article.html')


def update_article(request,*args,pk,**kwargs):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.author = request.POST.get('author')
        article.save()
        return redirect("article-detail", pk=article.pk)
    else:
        return render(request, 'update_article.html',{"article":article})


def article_detail(request, *args, pk, **kwargs):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'detail_article.html', {"article": article})

