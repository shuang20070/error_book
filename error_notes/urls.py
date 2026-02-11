# error_notes/urls.py 完整正确代码
from django.urls import path
# 导入当前app的views模块
from . import views

# 定义URL路由规则
urlpatterns = [
    # 错题列表页：访问 /notes/list/ 会触发 error_list 视图函数
    # name='error_list' 是模板中 {% url 'error_list' %} 对应的名称，必须完全一致
    path('list/', views.error_list, name='error_list'),

    # 错题详情页：访问 /notes/detail/数字/ 会触发 error_detail 视图函数
    # <int:pk> 用于接收错题的ID参数，name='error_detail' 对应模板中的跳转
    path('detail/<int:pk>/', views.error_detail, name='error_detail'),
]