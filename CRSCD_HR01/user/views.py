# coding=utf-8
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# 访问登录页
def login_request(request):
    red = render(request, 'user/login.html')
    url_next = request.GET.get('next', '/')
    red.set_cookie('url_next', url_next)
    return red


# 登录信息处理
def login_handle(request):
    if request.method == "POST":
        post = request.POST
        login_email = post['login_email']
        login_pwd = post['login_pwd']
        url_next = request.COOKIES.get('url_next', '/')
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
    logout(request)
    return redirect('/index/')


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
        return redirect('/user/login_request/')

    # 创建用户
    user = User.objects.create_user(username=user_email, password=user_pwd)
    user.email = user_email
    user.first_name = name[0]
    user.last_name = name[1:]
    user.save()

    # 注册成功，跳转登录页
    return redirect('/user/login_request/')


# 判断邮箱是否已经注册
def register_exist(request):
    username = request.GET.get('user_email')
    count = User.objects.filter(username=username).count()
    return JsonResponse({'count': count})





