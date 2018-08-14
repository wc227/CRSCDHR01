# coding=utf-8
from django.shortcuts import render, redirect
from login.models import *
from hashlib import sha1
from django.http import JsonResponse


# 登录页.
def login(request):
    return render(request, 'login/login.html')


# 注册信息处理
def register_handle(request):
    # 接受用户输入
    post = request.POST
    user_email = post.get('user_email')
    user_pwd = post.get('user_pwd')
    user_c_pwd = post.get('user_cpwd')
    user_phone = post.get('user_phone')

    # 判断输入密码是否一致
    if user_pwd != user_c_pwd:
        return redirect('/user/login/')

    # 密码加密
    s1 = sha1()
    s1.update(user_pwd.encode('utf8'))
    user_pwd_encode = s1.hexdigest()

    # 创建对象
    user = UserInfo()
    user.user_email = user_email
    user.user_pwd = user_pwd_encode
    user.user_phone = user_phone
    user.save()

    # 注册成功，跳转登录页
    return redirect('/user/login')


# 判断用户是否注册
def register_exist(request):
    user_email = request.GET.get('user_email')
    count = UserInfo.objects.filter(user_email=user_email).count()
    return JsonResponse({'count': count})

