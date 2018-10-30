# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.conf.urls import url
from . import views
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render


# 岗位创建
class Post(models.Model):
    """岗位信息"""

    # 岗位类型选项
    TYPE_CHOICES = (
        ('科研', '科研'),
        ('设计', '设计'),
        ('集成', '集成'),
        ('测试', '测试'),
        ('市场', '市场'),
        ('管理', '管理'),
    )

    # 公司选项
    COMPANY_CHOICES = (
        ('总部', '总部'),
        ('北京分公司', '北京分公司'),
        ('上海分公司', '上海分公司'),
        ('成都分公司', '成都分公司'),
        ('沈阳分公司', '沈阳分公司'),
        ('广州分公司', '广州分公司'),
        ('武汉分公司', '武汉分公司'),
        ('西安分公司', '西安分公司'),
        ('新疆分公司', '新疆分公司'),
        ('济南分公司', '济南分公司'),
        ('昆明分公司', '昆明分公司'),
        ('兰州分公司', '兰州分公司'),
        ('南昌分公司', '南昌分公司'),
        ('南宁分公司', '南宁分公司'),
        ('郑州分公司', '郑州分公司'),
    )

    # 招聘类型选型
    APPLY_CHOICES = (
        ('校园招聘', '校园招聘'),
        ('社会招聘', '社会招聘'),
    )

    # 工作年限选项
    EXP_CHOICES = (
        (0, '应届生'),
        (1, '一年以上'),
        (2, '二年以上'),
        (3, '三年以上'),
        (4, '四年以上'),
        (5, '五年以上'),
        (6, '六年以上'),
        (7, '七年以上'),
        (8, '八年以上'),
        (9, '九年以上'),
        (10, '十年以上'),
    )

    # 学历要求选项
    EDU_CHOICES = (
        ('本科', '本科'),
        ('研究生', '研究生'),
        ('博士生', '博士生'),
        ('专科', '专科'),
        ('不限', '不限'),
    )

    # 工作地选项
    LOCATION_CHOICES = (
        ('北京', '北京'),
        ('上海', '上海'),
        ('成都', '成都'),
        ('沈阳', '沈阳'),
        ('广州', '广州'),
        ('武汉', '武汉'),
        ('西安', '西安'),
        ('新疆', '新疆'),
        ('济南', '济南'),
        ('昆明', '昆明'),
        ('兰州', '兰州'),
        ('南昌', '南昌'),
        ('南宁', '南宁'),
        ('郑州', '郑州'),
    )

    post_name = models.CharField('岗位名称', max_length=10)
    post_type = models.CharField('岗位类型', max_length=10, choices=TYPE_CHOICES, default='综合管理')
    apply_type = models.CharField('招聘类型', max_length=10, choices=APPLY_CHOICES, default='社会招聘')
    company = models.CharField('所属公司', max_length=20, choices=COMPANY_CHOICES, default='总部',)
    location = models.CharField('工作地', max_length=10, choices=LOCATION_CHOICES, default='北京')
    department = models.CharField('所属部门', max_length=20)
    pub_date = models.DateField('发布时间')
    exp_date = models.DateField('到期时间', null=True, blank=True)
    exp_requirement = models.IntegerField('工作年限', choices=EXP_CHOICES, default=0)
    edu_requirement = models.CharField('学历要求', max_length=10, choices=EDU_CHOICES, default=0,)
    num = models.IntegerField('招聘人数', default=1)
    responsibilities = models.TextField('岗位描述', max_length=500)
    post_requirement = models.TextField('岗位要求', max_length=500)
    apply_num = models.IntegerField('应聘人数', default=0)
    fav_num = models.IntegerField('收藏人数', default=0)
    is_delete = models.BooleanField('是否删除', default=1)

    class Meta:
        verbose_name_plural = '岗位管理'


class PostApply(models.Model):
    """职位申请"""
    post = models.ForeignKey(Post, related_name="post", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="applicants", on_delete=models.CASCADE)
    status = models.CharField(max_length=10, default='申请中')
    is_delete = models.BooleanField(default=0)


class PostFav(models.Model):
    """职位收藏"""
    post = models.ForeignKey(Post, related_name="post_fav_foreignkey", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="favorites", on_delete=models.CASCADE)
    status = models.CharField(max_length=10, default='已收藏')
    is_delete = models.BooleanField(default=0)
