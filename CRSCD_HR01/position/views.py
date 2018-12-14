from django.shortcuts import render
from django.http import JsonResponse
from position import models
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from haystack.query import SearchQuerySet
from haystack.inputs import AutoQuery


# 校园招聘
def school_position(request):
    get = request.GET.get
    position_type = str(get('type'))       # 从页面获取岗位类型
    location = str(get('location'))        # 从页面获取工作地
    keyword = get('keyword')               # 从页面获取搜索关键字

    context = {
        'nav': 2,
        'title': '校园招聘',
        "position_type": position_type,
        "location": location,
    }                        # 构造返回数据

    if keyword:                            # 从搜索引擎获取职位
        results = SearchQuerySet().filter(content=AutoQuery(keyword), apply_type='校园招聘')  # 获取搜索结果
        positions = [r.object for r in results]  # 遍历搜索结果并生成职位列表
        context['keyword'] = keyword
    else:                                  # 从数据库获取校园招聘职位
        positions = models.Position.objects.filter(apply_type='校园招聘').order_by('-pub_date')

    # 职位类型筛选
    try:
        type_dic = {
            'development': '科研',
            'design': '设计',
            'integration': '集成',
            'testing': '测试',
            'market': '市场',
            'management': '管理',
        }  # 职位类型转义字典
        p_type = type_dic[position_type]  # 从字典中查找对应的职位类型
        positions = positions.filter(position_type=p_type)  # 根据职位类型进行筛选
    except KeyError:
        pass

    # 工作地筛选
    try:
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
    except KeyError:
        pass

    # 分页
    paginator = Paginator(positions, 8)
    page = request.GET.get('page')
    positions_page = paginator.get_page(page)
    context['positions'] = positions_page

    # 尝试获取登录用户姓名
    try:
        name = request.user.first_name + request.user.last_name
        context['name'] = name
    except AttributeError:
        pass

    return render(request, 'position/positionView.html', context)


# 社会招聘
def general_position(request):
    get = request.GET.get
    position_type = str(get('type'))       # 从页面获取岗位类型
    location = str(get('location'))        # 从页面获取工作地
    keyword = get('keyword')               # 从页面获取搜索关键字

    context = {
        'nav': 3,
        'title': '社会招聘',
        "position_type": position_type,
        "location": location,
    }                        # 构造返回数据

    if keyword:                            # 从搜索引擎获取职位
        results = SearchQuerySet().filter(content=AutoQuery(keyword), apply_type='社会招聘')  # 获取搜索结果
        positions = [r.object for r in results]  # 遍历搜索结果并生成职位列表
        context['keyword'] = keyword
    else:                                  # 从数据库获取校园招聘职位
        positions = models.Position.objects.filter(apply_type='社会招聘').order_by('-pub_date')

    # 职位类型筛选
    try:
        type_dic = {
            'development': '科研',
            'design': '设计',
            'integration': '集成',
            'testing': '测试',
            'market': '市场',
            'management': '管理',
        }  # 职位类型转义字典
        p_type = type_dic[position_type]  # 从字典中查找对应的职位类型
        positions = positions.filter(position_type=p_type)  # 根据职位类型进行筛选
    except KeyError:
        pass

    # 工作地筛选
    try:
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
    except KeyError:
        pass

    # 分页
    paginator = Paginator(positions, 8)
    page = request.GET.get('page')
    positions_page = paginator.get_page(page)
    context['positions'] = positions_page

    # 尝试获取登录用户姓名
    try:
        name = request.user.first_name + request.user.last_name
        context['name'] = name
    except AttributeError:
        pass

    return render(request, 'position/positionView.html', context)


# 职位申请和收藏
@login_required
def position_handle(request):
    """职位申请和职位收藏"""
    if request.user.is_authenticated:                       # 判断用户是否登录
        if hasattr(request.user, 'basic_info'):             # 判断用户是否维护了简历
            handle_type = request.GET.get('type')           # 获取职位操作类型
            position_id = request.GET.get('positionID')     # 获取职位ID
            position = models.Position.objects.get(id=position_id)  # 从数据库中查找ID对应的职位
            if handle_type == 'apply':                      # 职位申请
                models.PositionApply.objects.get_or_create(position=position, user=request.user)
            elif handle_type == 'fav':                      # 职位收藏
                models.PositionFav.objects.get_or_create(position=position, user=request.user)
            elif handle_type == 'applyCancel':              # 取消申请
                models.PositionApply.objects.filter(position=position).filter(user=request.user).delete()
            elif handle_type == 'favCancel':                # 取消收藏
                models.PositionFav.objects.filter(position=position).filter(user=request.user).delete()
            return JsonResponse({"success": 1})
        else:
            return JsonResponse({"success": 2})
    else:
        return JsonResponse({"success": 3})



