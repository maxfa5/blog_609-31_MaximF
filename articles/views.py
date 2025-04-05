from django.shortcuts import render
from .models import Article
# from web_prog.mysite.articles.models import Article

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_item(requset, slug):
    article = Article.objects.get(slug=slug)
    return render(requset, 'articles/article_item.html', {'article':article})