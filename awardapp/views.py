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