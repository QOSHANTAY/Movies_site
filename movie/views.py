from django.shortcuts import render,get_object_or_404,redirect
from . import models  
from .forms import Registration,LoginForm

from django.contrib.auth import login,logout,authenticate

def homepage(request):
    infos = models.Movie.objects.all()
    categories = models.Category.objects.all()
    return render(request,'index.html',{'ex':infos,'categories':categories})

def detail(request,id):
    movies = get_object_or_404(models.Movie,id = id)
    return render(request,'detail.html',{'detail':movies})

def category(request,slug):
    slug = get_object_or_404(models.Category,slug=slug)
    movies = models.Movie.objects.filter(categories = slug)
    return render(request,'category.html',{'movies':movies})

def base_cat(request):
    categories = models.Category.objects.all()
    return render(request,'base.html',{'categories':categories})

def registration(request):
    if request.method=='POST':
        forms = Registration(request.POST)
        if forms.is_valid():
            user = forms.save()
            login(request,user)
            return redirect('home')
    else:
        forms = Registration
    return render(request,'user/registration.html',{'forms':forms})


def log_out(request):
    logout(request)
    return redirect('home')

def log_in(request):
    if request.method=='POST':
        forms = LoginForm(request,request.POST)
        if forms.is_valid():
            user = forms.get_user()
            login(request,user)
            return redirect('home')
    else:
        forms = LoginForm
    return render(request,'user/login.html',{'forms':forms})
