# coding=utf-8
from django.shortcuts import render, redirect
from login.models import *
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse
from itsdangerous import URLSafeTimedSerializer as utsr
import base64
import re
from django.conf import settings as django_settings


# 登录页.
def login_request(request):
    username = request.COOKIES.get('username', '')
    context = {'title': '用户登录', 'error': 0, 'login_email': username}
    return render(request, 'login/login.html', context)


# 登录信息处理
def login_handle(request):
    # 获取登录信息
    post = request.POST
    login_email = post['login_email']
    login_pwd = post['login_pwd']
    user = authenticate(request, username=login_email, password=login_pwd)

    # 登录信息验证
    if user is not None:
        login(request, user)
        username = user.username
        name = user.first_name + user.last_name
        red = HttpResponseRedirect('/user/center')
        red.set_cookie('username', username)
        request.session['user_id'] = user.id
        request.session['name'] = name
        return red
    else:
        context = {'title': '用户登录', 'login_error': 1, 'login_email': login_email, 'login_pwd': login_pwd}
        return render(request, 'login/login.html/', context)


# 注册信息处理
def register_handle(request):
    # 接受用户输入
    post = request.POST
    user_email = post.get('user_email')
    user_pwd = post.get('user_pwd')
    user_c_pwd = post.get('user_cpwd')
    name = post.get('name')

    # 判断输入密码是否一致
    if user_pwd != user_c_pwd:
        return redirect('/user/login/')

    # 创建用户
    user = User.objects.create_user(username=user_email, password=user_pwd)
    user.email = user_email
    user.first_name = name[0]
    user.last_name = name[1:]
    user.save()

    # 注册成功，跳转登录页
    return redirect('/user/login')


# 判断邮箱是否已经注册
def register_exist(request):
    username = request.GET.get('user_email')
    count = User.objects.filter(username=username).count()
    return JsonResponse({'count': count})


# 个人中心
def center(request):
    return render(request, 'center.html')


