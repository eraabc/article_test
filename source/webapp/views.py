from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import ArticleForm
# from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404

from webapp.models import Article
from webapp.validation import validate


# Create your views here.
def index(request):
    articles = Article.objects.order_by('-created_at')
    return render(request, 'index.html', {"articles": articles})


def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect("article-detail", slug=article.slug)
        else:
            return render(request, 'create_article.html', {"form": form})
    else:
        form = ArticleForm()
        return render(request, 'create_article.html',{"form": form})


def update_article(request,*args,pk,**kwargs):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST,isinstance=article)
        if form.is_valid():
            article = form.save()
            return redirect("article-detail", slug=article.slug)
        else:
            return render(request, 'update_article.html', {"form": form})
    else:
        form = ArticleForm(instance=article)
        return render(request, 'update_article.html',{"form": form})


def delete_article(request,*args,pk,**kwargs):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        article.delete()
        return redirect("index")
    else:
        return  render(request,'delete_article.html',{'article':article})


def article_detail(request, *args, slug, **kwargs):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'detail_article.html', {"article": article})

