from django.shortcuts import render
from django.http import JsonResponse
from . import models


# 校园招聘
def school_position(request):
    user_name = request.user.first_name + request.user.last_name
    positions = models.Post.objects.filter(apply_type='校园招聘')
    context = {
        'positions': positions,
        'nav': 2,
        'name': user_name,
    }
    return render(request, 'post/postView.html', context)


# 社会招聘
def general_position(request):
    user_name = request.user.first_name + request.user.last_name
    positions = models.Post.objects.filter(apply_type='社会招聘')
    context = {
        'positions': positions,
        'nav': 3,
        'name': user_name,
    }
    return render(request, 'post/postView.html', context)








# 职位申请和职位收藏
def post_handle(request):
    """职位申请和职位收藏"""
    handle_type = request.GET.get('type')
    post_id = request.GET.get('positionID')
    post = models.Post.objects.get(id=post_id)
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


