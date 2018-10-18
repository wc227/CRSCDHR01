from django.contrib import admin
from . import models


def refresh_apply_fav(modeladmin, request, queryset):
    """刷新职位申请与职位收藏情况"""
    post = models.Post.objects.all()
    for p in post:
        post_apply = models.PostApply.objects.filter(post=p)
        post_fav = models.PostFav.objects.filter(post=p)
        p.apply_num = post_apply.count()
        p.fav_num = post_fav.count()
        p.save()


refresh_apply_fav.short_description = "刷新申请情况"


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):

    # 设置默认排序字段
    ordering = ('department', '-public_date')

    # 设置列表可编辑字段
    # list_editable = ['department', 'num', 'company']

    # 设置显示外键字段
    # fk_fields = ('123')

    # 设置进入编辑界面的链接字段
    list_display_links = ['post_name']

    # 设置在列表中显示的字段
    list_display = [
        'id',
        'post_name',
        'apply_num',
        'fav_num',
        'company',
        'department',
        'edu_requirement',
        'exp_requirement',
        'num',
        'public_date',
    ]

    actions = [refresh_apply_fav]
