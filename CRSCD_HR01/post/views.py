from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from . import models


# 浏览岗位
def post_view(request):
    post_id = request.GET.getlist('postID')

    return render(request, 'index.html', {'post_id': post_id})


# 申请岗位
def post_handle(request):
    handle_type = request.GET.get('type')
    post_id = request.GET.get('positionID')
    post = models.Post.objects.get(id=post_id)
    if handle_type == 'apply':
        post.applicants.add(request.user)
        post.apply_num = post.applicants.count()
    elif handle_type == 'fav':
        post.favorites.add(request.user)
        post.fav_num = post.favorites.count()
    post.save()
    return JsonResponse({"success": 1})


