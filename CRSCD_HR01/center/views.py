from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import os
from django.contrib.auth.decorators import login_required
from django.core.files import File
from . import models


resume_count = 0

#  创建简历
@login_required
def resume_create(request):
    name = request.user.first_name + request.user.last_name
    return render(request, 'center/resume.html', {'name': name})


#  上传简历
@login_required
def resume_up(request):
    if request.method == 'GET':
        resume_list = models.Resume.objects.all()
        return render(request, 'center/resume.html/', {'resume_list': resume_list})
    elif request.method == 'POST':
        resume = request.FILES['resume_file']
        file_name = str(request.user.id) + request.user.first_name + request.user.last_name + '-' + resume.name
        resume_path = settings.MEDIA_ROOT + '/resume/' + file_name
        with open(resume_path, 'wb+') as f:
            resume_file = File(f)
            for chunk in resume.chunks():
                resume_file.write(chunk)
        return JsonResponse({'file_name': file_name}, safe=False)


#  删除简历
@login_required()
def resume_del(request):
    print(request.resume_path)
    print('-'*20)
    os.remove(request.resume_path)

