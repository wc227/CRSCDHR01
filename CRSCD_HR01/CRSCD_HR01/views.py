from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from post import models


def index(request):
    name = request.user.first_name + request.user.last_name
    post = models.Post.objects.all()
    context = {
        'name': name,
        'post': post,
    }
    return render(request, 'index.html', context)

