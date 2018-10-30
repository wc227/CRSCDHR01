from django.shortcuts import render, redirect
from django.http import JsonResponse
from post import models
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# 校园招聘
def school_position(request):
    positions = models.Post.objects.filter(apply_type='校园招聘').order_by('-public_date')
    paginator = Paginator(positions, 2, allow_empty_first_page=True)
    page = request.GET.get('page')
    positions_display = paginator.get_page(page)
    try:
        name = request.user.first_name + request.user.last_name
        context = {'name': name, 'positions': positions_display, 'nav': 2, 'title': '校园招聘'}
    except:
        context = {'positions': positions_display, 'nav': 2, 'title': '校园招聘'}
    return render(request, 'post/postView.html', context)





# 社会招聘
def general_position(request):
    positions = models.Post.objects.filter(apply_type='社会招聘')
    try:
        name = request.user.first_name + request.user.last_name
        context = {'name': name, 'positions': positions, 'nav': 3, 'title': '社会招聘'}
    except:
        context = {'positions': positions, 'nav': 3, 'title': '社会招聘'}
    return render(request, 'post/postView.html', context)





# 职位申请和职位收藏
@login_required
def post_handle(request):
    """职位申请和职位收藏"""
    handle_type = request.GET.get('type')
    post_id = request.GET.get('positionID')
    post = models.Post.objects.get(id=post_id)
    if request.user is not None:
        # 职位申请
        if handle_type == 'apply':
            models.PostApply.objects.get_or_create(post=post, user=request.user)

        # 职位收藏
        elif handle_type == 'fav':
            models.PostFav.objects.get_or_create(post=post, user=request.user)

        # 取消申请
        elif handle_type == 'applyCancel':
            models.PostApply.objects.filter(post=post).filter(user=request.user).delete()

        # 取消收藏
        elif handle_type == 'favCancel':
            models.PostFav.objects.filter(post=post).filter(user=request.user).delete()

        return JsonResponse({"success": 1})
    else:
        return JsonResponse({"success": 0})


