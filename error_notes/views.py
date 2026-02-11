from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Django 错题本首页 — 第一天任务完成！")
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Django 错题本首页 — 第一天任务完成！")

# 新增：错题列表视图
def error_list(request):
    return HttpResponse("这是错题列表页面")

# 新增：错题详情视图
def error_detail(request, pk):
    return HttpResponse(f"这是第 {pk} 道错题的详情页面")
from django.shortcuts import render, get_object_or_404
from .models import ErrorNote

# 错题列表页视图
def error_list(request):
    # 获取所有错题，并按创建时间倒序排列
    errors = ErrorNote.objects.all().order_by('-create_at')
    return render(request, 'error_notes/list.html', {'errors': errors})

# 错题详情页视图
def error_detail(request, pk):
    # 根据ID获取单个错题，不存在则返回404页面
    error = get_object_or_404(ErrorNote, pk=pk)
    return render(request, 'error_notes/detail.html', {'error': error})