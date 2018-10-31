from django.shortcuts import render, redirect
from django.http import JsonResponse
from position import models
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from haystack.views import SearchView


# 校园招聘
def school_position(request):
    # 从数据库获取全部校园招聘岗位
    positions = models.Position.objects.filter(apply_type='校园招聘').order_by('-pub_date')
    position_type = str(request.GET.get('type'))  # 从页面获取岗位类型
    location = str(request.GET.get('location'))  # 从页面获取工作地

    if position_type != 'None':  # 职位类型筛选
        type_dic = {
            'development': '科研',
            'design': '设计',
            'integration': '集成',
            'testing': '测试',
            'market': '市场',
            'management': '管理',
        }  # 职位类型转义字典
        city = type_dic[position_type]  # 从字典中查找对应的职位类型
        positions = positions.filter(position_type=city)  # 根据职位类型进行筛选
    if location != 'None':  # 工作地筛选
        location_dic = {
            'bj': '北京',
            'sh': '上海',
            'gz': '广州',
            'xa': '西安',
            'sy': '沈阳',
            'wh': '武汉',
            'cd': '成都',
            'xj': '新疆',
        }  # 工作地转义字典
        city = location_dic[location]  # 从字典查找对应的城市
        positions = positions.filter(location=city)  # 根据工作地进行筛选

    # 分页
    paginator = Paginator(positions, 2)
    page = request.GET.get('page')
    positions_page = paginator.get_page(page)

    # 构造返回数据
    context = {
        'nav': 2,
        'title': '校园招聘',
        "positions": positions_page,
        "position_type": position_type,
        "location": location,
    }

    # 尝试获取登录用户姓名
    try:
        name = request.user.first_name + request.user.last_name
        context['name'] = name
    except AttributeError:
        pass

    return render(request, 'position/positionView.html', context)


# 社会招聘
def general_position(request):
    positions = models.Position.objects.filter(apply_type='社会招聘')
    position_type = str(request.GET.get('type'))  # 从页面获取岗位类型
    location = str(request.GET.get('location'))  # 从页面获取工作地

    if position_type != 'None':  # 职位类型筛选
        type_dic = {
            'development': '科研',
            'design': '设计',
            'integration': '集成',
            'testing': '测试',
            'market': '市场',
            'management': '管理',
        }  # 职位类型转义字典
        position_type = type_dic[position_type]  # 从字典中查找对应的职位类型
        positions = positions.filter(position_type=position_type)  # 根据职位类型进行筛选
    if location != 'None':  # 工作地筛选
        location_dic = {
            'bj': '北京',
            'sh': '上海',
            'gz': '广州',
            'xa': '西安',
            'sy': '沈阳',
            'wh': '武汉',
            'cd': '成都',
            'xj': '新疆',
        }  # 工作地转义字典
        city = location_dic[location]  # 从字典查找对应的城市
        positions = positions.filter(location=city)  # 根据工作地进行筛选

    # 分页
    paginator = Paginator(positions, 2)
    page = request.GET.get('page')
    positions_page = paginator.get_page(page)

    # 构造返回数据
    context = {
        'nav': 2,
        'title': '社会招聘',
        "positions": positions_page,
        "position_type": position_type,
        "location": location,
    }

    # 尝试获取登录用户姓名
    try:
        name = request.user.first_name + request.user.last_name
        context['name'] = name
    except AttributeError:
        pass

    return render(request, 'position/positionView.html', context)


# 职位搜索
class PositionSearchView(SearchView):
    template = 'position/positionView.html'




# 职位申请和收藏
@login_required
def position_handle(request):
    """职位申请和职位收藏"""
    handle_type = request.GET.get('type')
    position_id = request.GET.get('positionID')
    position = models.Position.objects.get(id=position_id)
    if request.user is not None:
        # 职位申请
        if handle_type == 'apply':
            models.PositionApply.objects.get_or_create(position=position, user=request.user)

        # 职位收藏
        elif handle_type == 'fav':
            models.PositionFav.objects.get_or_create(position=position, user=request.user)

        # 取消申请
        elif handle_type == 'applyCancel':
            models.PositionApply.objects.filter(position=position).filter(user=request.user).delete()

        # 取消收藏
        elif handle_type == 'favCancel':
            models.PositionFav.objects.filter(position=position).filter(user=request.user).delete()

        return JsonResponse({"success": 1})
    else:
        return JsonResponse({"success": 0})


