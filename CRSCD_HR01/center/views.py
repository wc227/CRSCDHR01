from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from post.models import Post, PostApply, PostFav
import os
from django.contrib.auth.decorators import login_required
from . import models
from django.core.exceptions import ObjectDoesNotExist


# 上传简历附件
@login_required
def resume_up(request):
    """上传简历附件"""
    if request.method == 'POST':
        resume_file = request.FILES['resume_file']
        # 用户信息
        user_id = str(request.user.id)
        user_name = request.user.first_name + request.user.last_name
        rear = os.path.splitext(resume_file.name)[1]
        # 原文件名
        file_name = resume_file.name
        # 修改后文件名
        resume_file.name = user_id + '-' + user_name + '-简历' + rear
        # 删除既有简历
        try:
            exist_file = models.ResumeFile.objects.filter(user__exact=request.user.id)
            for e in exist_file:
                e.resume_file.delete()
                e.delete()
        except ObjectDoesNotExist:
            pass
        # 创建用户外键
        u = User.objects.get(id=request.user.id)
        # 实例化文件
        models.ResumeFile.objects.create(file_name=file_name, resume_file=resume_file, user=u)
        return JsonResponse({'success': 1})


# 删除简历附件
@login_required()
def resume_del(request):
    """删除简历附件"""
    try:
        exist_file = models.ResumeFile.objects.filter(user=request.user.id)
        for e in exist_file:
            e.resume_file.delete()
            e.delete()
    except ObjectDoesNotExist:
        pass
    return JsonResponse({'delete': 1})


# 提交简历
@login_required()
def resume_submit(request):
    """提交简历表单"""
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
        work_list = models.WorkInfo.objects.filter(work_foreignkey__exact=request.user.id)
        for w in work_list:
            w.delete()
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
        edu_list = models.EduInfo.objects.filter(edu_foreignkey__exact=request.user.id)
        for e in edu_list:
            e.delete()
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
    """浏览简历"""
    user = User.objects.get(id=request.user.id)
    work_info = models.WorkInfo.objects.filter(work_foreignkey__exact=request.user.id)
    work_len = work_info.count()
    edu_info = models.EduInfo.objects.filter(edu_foreignkey__exact=request.user.id)
    try:
        file = models.ResumeFile.objects.get(user__exact=request.user.id)
    except ObjectDoesNotExist:
        file = None
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
            'file': file,
            'view_para': 1,
            'work_len': work_len,
        }

    else:
        context = {
            # 用于前端欢迎您的姓名
            'name': request.user.first_name + request.user.last_name,
            'view_para': 0,
        }

    # 用于前端导航条active的参数
    context['active'] = 1
    context['nav'] = 5
    context['title'] = '个人中心'

    return render(request, 'center/resume.html', context)


# 修改简历
@login_required()
def resume_modify(request):
    user = User.objects.get(id=request.user.id)
    work_info = models.WorkInfo.objects.filter(work_foreignkey__exact=request.user.id)
    work_len = work_info.count()
    edu_info = models.EduInfo.objects.filter(edu_foreignkey__exact=request.user.id)
    edu_len = edu_info.count()
    try:
        file = models.ResumeFile.objects.get(user=request.user.id)
    except ObjectDoesNotExist:
        file = None
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
        'work_len': work_len,
        'edu_len': edu_len,
        'file': file,
        'active': 1,
    }
    return render(request, 'center/resume.html', context)


# 删除工作条目
@login_required()
def work_del(request):
    if request.method == 'GET':
        work_id = request.GET.get('workId')
        try:
            models.WorkInfo.objects.filter(id=work_id).delete()
            work_len = models.WorkInfo.objects.filter(work_foreignkey__exact=request.user.id).count()
            return JsonResponse({'work_len': work_len})
        except ValueError:
            pass


# 删除教育条目
@login_required()
def edu_del(request):
    if request.method == 'GET':
        edu_id = request.GET.get('eduId')
        try:
            models.EduInfo.objects.filter(id=edu_id).delete()
            edu_len = models.EduInfo.objects.filter(edu_foreignkey__exact=request.user.id).count()
            return JsonResponse({'edu_len': edu_len})
        except ValueError:
            pass


# 访问个人中心我的申请、我的收藏
@login_required()
def post_view(request):
    """访问个人中心我的申请、我的收藏"""
    req_type = request.GET.get('type')
    apply_info = PostApply.objects.filter(user_foreignkey=request.user)
    apply_list = []
    fav_list = []
    for a in apply_info:
        post = a.post_foreignkey
        apply_list.append(post)
    fav_info = PostFav.objects.filter(user_foreignkey=request.user)
    for f in fav_info:
        fav = f.post_foreignkey
        fav_list.append(fav)
    context = {
        'post_applied': apply_list,
        'post_fav': fav_list,
        'type': req_type,
        'name': request.user.first_name + request.user.last_name,
        'active': req_type,
        'nav': 5,
    }
    return render(request, 'center/resume_post.html', context)


# 浏览职位详情
@login_required()
def post_modal(request):
    """浏览职位详情"""
    post_id = request.GET.get('postId')
    position = Post.objects.get(id=post_id)
    context = {
        'post_name': position.post_name,
        'post_type': position.post_type,
        'apply_type': position.apply_type,
        'post_company': position.company,
        'post_location': position.location,
        'department': position.department,
        'public_date': position.public_date,
        'expire_date': position.expire_date,
        'exp_requirement': position.exp_requirement,
        'edu_requirement': position.edu_requirement,
        'num': position.num,
        'responsibilities': position.responsibilities,
        'post_requirement': position.post_requirement,

    }
    return JsonResponse(context)
