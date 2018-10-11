from django.contrib import admin
from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    # 设置在列表中显示的字段
    list_display = [
        'id',
        'post_name',
        'apply_num',
        'company',
        'department',
        'edu_requirement',
        'exp_requirement',
        'num',
        'public_date',
    ]

    # 设置默认排序字段
    ordering = ('department', '-public_date')

    # 设置列表可编辑字段
    # list_editable = ['department', 'num', 'company']

    # 设置显示外键字段
    # fk_fields = ('123')

    # 设置进入编辑界面的链接字段
    list_display_links = ['post_name']


