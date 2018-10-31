from django.contrib import admin
from . import models


def refresh_apply_fav(modeladmin, request, queryset):
    """刷新职位申请与职位收藏情况"""
    position = models.Position.objects.all()
    for p in position:
        position_apply = models.PositionApply.objects.filter(position=p)
        position_fav = models.PositionFav.objects.filter(position=p)
        p.apply_num = position_apply.count()
        p.fav_num = position_fav.count()
        p.save()


refresh_apply_fav.short_description = "刷新申请情况"


@admin.register(models.Position)
class PositionAdmin(admin.ModelAdmin):

    # 设置默认排序字段
    ordering = ('department', '-pub_date')

    # 设置列表可编辑字段
    # list_editable = ['department', 'num', 'company']

    # 设置显示外键字段
    # fk_fields = ('123')

    # 设置进入编辑界面的链接字段
    list_display_links = ['position_name']

    # 设置在列表中显示的字段
    list_display = [
        'id',
        'position_name',
        'apply_num',
        'fav_num',
        'company',
        'department',
        'edu_req',
        'exp_req',
        'num',
        'pub_date',
    ]

    actions = [refresh_apply_fav]
