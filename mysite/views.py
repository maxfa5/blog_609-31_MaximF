# from django.http import HttpResponse

from django.shortcuts import render
from articles.models import Article
from django.templatetags.static import static

def homepage(request):
    data = {"header": "Homepage", "message": "Welcome to my site!"}
    articles = Article.objects.order_by('date')[:2]

    return render(request, 'homepage.html', context={"data": data, "articles":articles})


def about(request):
    header = "About Us"
    staff = ['John Nichols', "John Mirty", 'Timoty Smidth']
    director = {"name": "David Lee", "img": '/director.jpg'}
    address = ('20 W 43 st.', "New York", "NY 1001", 'USA')
    Contacts = ["https://github.com/maxfa5","@Sandajer","+7........"]
    data = {"header": header,"staff": staff, "director": director, "address":address, "Contacts":Contacts}
    img = static("cat.jpg")
    return render(request, 'about.html', data)

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout


def signup_view(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/articles')
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect('/articles')
    else:
        print("Not coorect")
        form = AuthenticationForm()
    return render(request,'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method =='POST':
        logout(request)
    return HttpResponseRedirect('/articles')