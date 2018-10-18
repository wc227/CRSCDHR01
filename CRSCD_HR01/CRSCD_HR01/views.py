from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from post import models


def index(request):
    try:
        name = request.user.first_name + request.user.last_name
        post = models.Post.objects.all()
        context = {
            'name': name,
            'post': post,
        }
    except:
        context = {}
    return render(request, 'index.html', context)

