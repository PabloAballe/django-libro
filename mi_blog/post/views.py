from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm

def home(request):
    if request.user.is_authenticated:

        post=Post.objects.all().order_by('-fecha_de_creacion')
        if request.method == "POST":
            form = SheachForm(request.POST)
            if form.is_valid():
                print("El fomrulario es valido ")
                q= form.cleaned_data['shearch']
                post=Post.objects.all().order_by('-fecha_de_creacion').filter(articulo__contains=q)
                print(f"se busco {q}")
        else:
            form=SheachForm()
        context={'post': post, 'form': form}
        return render(request, 'home.html',context)
    return redirect('login')

def post(request, pk):
    post=Post.objects.get(pk=pk)
    context={'post': post}
    return render(request, 'post.html',context)

def logout(request):
    do_logout(request)
    return redirect('home')

def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)


            if user is not None:
                do_login(request, user)
                return redirect('home')


    return render(request, "login.html", {'form': form})

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                do_login(request, user)
                return redirect('home')

    return render(request, "register.html", {'form': form})
