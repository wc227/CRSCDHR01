from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def index(request):
    try:
        first_name = request.user.first_name
        last_name = request.user.last_name
        context = {'name': first_name + last_name}
        return render(request, 'index.html', context)
    except:
        return render(request, 'index.html')
