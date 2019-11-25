import datetime as dt
from django.http import HttpResponse,Http404,HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from .email import *
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from rest_framework import status
from .permissions import *
from .serializer import *
from rest_framework import status
from .permissions import IsAdminOrReadOnly

# Create your views here.
def homepage(request):
    posts = Post.all_posts()
    profile = Profile.get_all_profiles()
    ratings=Ratings.objects.all()
    current_user = request.user
    context =  {
        "profile": profile,
        "posts":posts ,
        "ratings":ratings,
    }
    return render(request, 'index.html', context)

@login_required(login_url='/accounts/login/')
def add_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_profile = current_user
            post.save()
        return redirect('homepage')

    else:
        form = UploadForm()
    return render(request, 'upload.html', {"form": form})    

@login_required(login_url='/accounts/login/')
def profile(request, username):
    profile = User.objects.get(username=username)
    try:
        profile_info = Profile.get_profile(profile.id)
    except:
        profile_info = Profile.filter_by_id(profile.id)
    posts = Post.get_profile_image(profile.id)
    title = f'@{profile.username}'
    return render(request, 'profile.html', {'title':title, 'profile':profile, 'profile_info':profile_info, 'posts':posts})  

@login_required(login_url='/accounts/login/')
def add_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('homepage')

def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        posts_results = Post.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"posts": posts_results})

    else:
        message = "Please enter a search term"
        return render(request, 'search.html',{"message":message})        

    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form": form})      