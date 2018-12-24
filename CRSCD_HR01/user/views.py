from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import json

# 登录
def log_in(request):
    """登录"""
    url_prev = request.GET.get('next')
    if url_prev:
        url_next = url_prev
    else:
        url_next = '/index/'
    red = render(request, 'user/login.html', {'title': '用户登录'})
    red.set_cookie('url_next', url_next)
    return red


# 登录信息验证
def login_handle(request):
    """登录信息验证"""
    if request.method == "POST":
        post = request.POST
        login_email = post['login_email']
        login_pwd = post['login_pwd']
        url_next = request.COOKIES['url_next']
        user = authenticate(request, username=login_email, password=login_pwd)

    # 登录信息验证
        if user is not None:
            login(request, user)
            return redirect(url_next)
        else:
            context = {'title': '用户登录', 'login_error': 1, 'login_email': login_email, 'login_pwd': login_pwd}
            return render(request, 'user/login.html/', context)


# 注销登录
def log_out(request):
    """注销登录"""
    logout(request)
    return redirect('/index/')


# 注册信息处理
def register_handle(request):
    """注册信息处理"""

    # 接收用户输入
    post = request.POST
    user_email = post.get('user_email')
    user_pwd = post.get('user_pwd')
    user_c_pwd = post.get('user_cpwd')
    name = post.get('name')

    # 判断输入密码是否一致
    if user_pwd != user_c_pwd:
        return redirect('/user/login_request/')

    # 创建用户
    user = User.objects.create_user(username=user_email, password=user_pwd)
    user.email = user_email
    user.first_name = name[0]
    user.last_name = name[1:]
    user.save()

    # 注册成功，跳转登录页
    return redirect('/user/logIn/')


# 判断邮箱是否已经注册
def register_exist(request):
    """判断邮箱是否已经注册"""
    username = request.GET.get('user_email')
    count = User.objects.filter(username=username).count()
    return JsonResponse({'count': count})


# 判断原始密码是否正确
def pre_pwd_check(request):
    pre_pwd = request.POST['prePwd']
    username = request.user.username
    user = authenticate(username=username, password=pre_pwd)
    if user is not None:
        return JsonResponse({"success": 1})
    else:
        return JsonResponse({"success": 2})


# 更改密码
@login_required
@require_POST
def change_pwd(request):
    """用户自主更改密码"""
    new_pwd = request.POST['newPwd']
    print(new_pwd)
    username = request.user.username
    user = User.objects.get(username=username)
    user.set_password(new_pwd)
    user.save()

    return render(request, "user/login.html")


# 更改邮箱
@login_required
@require_POST
def change_email(request):
    """更改邮箱"""
    new_email = request.POST['newEmail']
    username = request.user.username
    user = User.objects.get(username=username)
    user.username = new_email
    user.email = new_email
    user.save()
    logout(request)
    return render(request, "user/login.html")


# 注册声明
def register_agreement(request):
    """注册声明"""
    context = {
        "title": "隐私协议"
    }
    return render(request, 'user/register_agreement.html', context)

