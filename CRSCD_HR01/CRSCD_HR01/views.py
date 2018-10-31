from django.shortcuts import render
from position.models import Position


def index(request):
    position = Position.objects.order_by('-pub_date')[:4]
    try:
        name = request.user.first_name + request.user.last_name
        context = {'name': name, 'position': position}
    except:
        context = {'position': position}
    return render(request, 'index.html', context)

