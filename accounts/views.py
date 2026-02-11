from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# 用户注册
def signup(request):
    return HttpResponse("这是用户注册页面")

# 用户登录
def login(request):
    return HttpResponse("这是用户登录页面")

# 用户退出
def logout(request):
    return HttpResponse("你已成功退出登录")
