from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings


# Create your views here.


# 个人中心
def resume(request):
    return render(request, 'center/resume.html')


def photo_upload_handle(request):
    photo = request.FILES['photo']
    photo_name = photo.name
    photo_path = os.path.join(settings.MEDIA_ROOT, photo.name)
    with open(photo_path, 'wb+') as pic:
        for c in photo.chunks():
            pic.write(c)
    text = {'photo_name': photo_name}
    return render(request, 'center/resume.html', text)
