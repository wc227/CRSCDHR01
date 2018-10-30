from django.shortcuts import render
from post import models


def index(request):
    post = models.Post.objects.order_by('-public_date')[:4]
    try:
        name = request.user.first_name + request.user.last_name
        context = {'name': name, 'post': post}
    except:
        context = {'post': post}
    return render(request, 'index.html', context)

