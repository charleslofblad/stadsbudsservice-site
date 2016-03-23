from django.shortcuts import render
from django.utils import timezone
from .models import Article
from django.shortcuts import render, get_object_or_404

# Create your views here.
#def article_list(request):
#    return render(request, 'article/article_list.html', {})

def article_list(request):
    articles = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'article/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article/article_detail.html', {'article': article})

def index_view(request):
    return render(request, 'index.html', {})