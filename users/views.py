from django.shortcuts import render
from django.views import generic
from .forms import RegisterUserForm, CreatePostForm, LoginUserForm
from .models import *
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def register_request(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("users:profile")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = RegisterUserForm()
    return render (request=request, template_name="users/register.html", context={"register_form":form})


def login_request(request):
    form = LoginUserForm(request.POST)
    if request.method == "POST":
        print('post start ')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Log-in Successfully')
        else:
            messages.error(request, form.errors)
    return render(request=request, template_name="users/login.html", context={"login_form":form})    


def logout_request(request):
    logout(request)
    messages.success(request, "You have successfully logged out.") 
    return redirect("users:login")

@login_required
def profile_request(request):
    return render (request=request, template_name="users/profile.html")

@login_required
def create_post(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            messages.success(request, f'Post created Successfully')
            return redirect("users:profile")
    else:
        form = CreatePostForm()
    return render(request, 'users/create_post.html', {'form':form})


@login_required
def post_list(request):
    post = Post.objects.filter(user=request.user)
    return render(request, 'users/all_post.html', {'posts':post})