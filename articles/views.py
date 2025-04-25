from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Article
from django.shortcuts import redirect
from . import forms


# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})
    # return render(request, 'homepage.html')

def article_item(requset, slug):
    article = Article.objects.get(slug=slug)
    print(article)
    return render(requset, 'articles/article_item.html', {'article':article})

@login_required(login_url='accounts:login')
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author =request.user
            instance.save()
            return redirect('articles:articlesList')
    else:
        form = forms.CreateArticle() 
    return render(request, 'articles/article_create.html', {'form': form})