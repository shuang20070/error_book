from django.shortcuts import render
from .models import ErrorNote

def index(request):
    # 这里不再返回纯文本，而是渲染模板
    return render(request, 'error_notes/index.html', {
        'page_title': '我的错题列表'
    })