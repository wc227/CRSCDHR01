from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from . import models


# 职位申请和职位收藏
def post_handle(request):
    """职位申请和职位收藏"""
    handle_type = request.GET.get('type')
    post_id = request.GET.get('positionID')
    post = models.Post.objects.get(id=post_id)
    if handle_type == 'apply':
        apply = models.PostApply.objects.get_or_create(post_foreignkey=post, user_foreignkey=request.user)
        apply[0].apply_status = "申请中"
        apply[0].save()
    elif handle_type == 'fav':
        models.PostFav.objects.get_or_create(post_foreignkey=post, user_foreignkey=request.user)
    return JsonResponse({"success": 1})


