from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth.models import User
import os
import re
from django.contrib.auth.decorators import login_required
from django.core.files import File
from django.core.files.storage import default_storage
from . import models

resume_count = 0

'''
#  创建简历
@login_required
def resume(request):
    name = request.user.first_name + request.user.last_name
    view_para = 0
    context = {
        'name': name,
        'view_para': view_para,
    }
    return render(request, 'center/resume.html', context)
'''

# 上传简历附件
@login_required
def resume_up(request):
    if request.method == 'GET':
        resume_list = models.Resume.objects.all()
        return render(request, 'center/resume.html/', {'resume_list': resume_list})
    elif request.method == 'POST':
        resume = request.FILES['resume_file']
        resume_rear = os.path.splitext(resume.name)[1]
        file_name = str(request.user.id) + '-' + request.user.first_name + request.user.last_name + resume_rear
        global resume_path
        resume_path = settings.MEDIA_ROOT + '/resume/' + file_name
        with open(resume_path, 'wb+') as f:
            resume_file = File(f)
            for chunk in resume.chunks():
                resume_file.write(chunk)
        return JsonResponse({'file_name': file_name}, safe=False)


# 删除简历附件
@login_required()
def resume_del(request):
    default_storage.delete(resume_path)
    return JsonResponse({'delete': 1})


# 提交简历
@login_required()
def resume_submit(request):
    if request.method == 'POST':
        post = request.POST

        # 获取基本信息
        name = post.get('name')
        phone = post.get('phone')
        age = post.get('age')
        work_year = post.get('work_year')
        party = post.get('party')
        live_location = post.get('live_location')
        study_location = post.get('study_location')
        identity_id = post.get('identity_id')
        if int(identity_id[-2]) % 2 == 0:
            gender = '女'
        else:
            gender = '男'

        # 获取工作信息
        company = post.getlist('company', '')
        position = post.getlist('position', '')
        work_stime = post.getlist('work_stime', '')
        work_etime = post.getlist('work_etime', '')
        work_desc = post.getlist('work_desc', '')

        # 获取学历信息
        school = post.getlist('school')
        profession = post.getlist('profession')
        education = post.getlist('education')
        degree = post.getlist('degree')
        school_stime = post.getlist('edu_stime')
        school_etime = post.getlist('edu_etime')
        profession_desc = post.getlist('profession_desc')

        # 存储基本信息
        user_id = request.user.id
        u = User.objects.get(id=user_id)
        basic_info = models.BasicInfo()
        basic_info.id = user_id
        basic_info.user = u
        basic_info.name = name
        u.first_name = name[0]
        u.last_name = name[1:]
        basic_info.phone = phone
        basic_info.age = age
        basic_info.work_year = work_year
        basic_info.party = party
        basic_info.live_location = live_location
        basic_info.study_location = study_location
        basic_info.identity_id = identity_id
        basic_info.gender = gender
        basic_info.save()
        u.save()

        # 存储工作信息

        for c, p, s, e, d in zip(company, position, work_stime, work_etime, work_desc):
            models.WorkInfo.objects.create(
                company=c,
                position=p,
                work_stime=s,
                work_etime=e,
                work_desc=d,
                work_foreignkey=basic_info,
            )

        # 存储学历信息

        for s, p, e, d, ss, se, pd in zip(
            school, profession, education, degree, school_stime, school_etime, profession_desc
        ):
            models.EduInfo.objects.create(
                school=s,
                profession=p,
                education=e,
                degree=d,
                school_stime=ss,
                school_etime=se,
                profession_desc=pd,
                edu_foreignkey=basic_info
            )
        return redirect('/center/resume/')


# 浏览简历
@login_required()
def resume(request):
    user = User.objects.get(id=request.user.id)
    work_list = models.WorkInfo.objects.filter(work_foreignkey__exact=request.user.id)
    work_info = work_list
    edu_list = models.EduInfo.objects.filter(edu_foreignkey__exact=request.user.id)
    edu_info = edu_list
    if hasattr(user, 'basic_info'):
        context = {
            # 传输基本信息
            'name': user.basic_info.name,
            'email': user.email,
            'phone': user.basic_info.phone,
            'age': user.basic_info.age,
            'work_year': user.basic_info.work_year,
            'identity_id': user.basic_info.identity_id,
            'gender': user.basic_info.gender,
            'live_location': user.basic_info.live_location,
            'study_location': user.basic_info.study_location,
            'party': user.basic_info.party,
            'work_info': work_info,
            'edu_info': edu_info,
            'view_para': 1,
        }

    else:
        context = {
            'name': request.user.first_name + request.user.last_name,
            'view_para': 0,
        }
    return render(request, 'center/resume.html', context)


# 修改简历
@login_required()
def resume_modify(request):
    user = User.objects.get(id=request.user.id)
    work_list = models.WorkInfo.objects.filter(work_foreignkey__exact=request.user.id)
    work_info = work_list
    edu_list = models.EduInfo.objects.filter(edu_foreignkey__exact=request.user.id)
    edu_info = edu_list
    context = {
        'name': user.basic_info.name,
        'email': user.email,
        'phone': user.basic_info.phone,
        'age': user.basic_info.age,
        'work_year': user.basic_info.work_year,
        'identity_id': user.basic_info.identity_id,
        'gender': user.basic_info.gender,
        'live_location': user.basic_info.live_location,
        'study_location': user.basic_info.study_location,
        'party': user.basic_info.party,
        'work_info': work_info,
        'edu_info': edu_info,
        'view_para': 0,
    }
    return render(request, 'center/resume.html', context)
