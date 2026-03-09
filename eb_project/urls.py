from django.contrib import admin
from django.urls import path
# 导入error_notes应用的视图
from error_notes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 新增：根路径 / 对应index视图，命名为index
    path('', views.index, name='index'),
    # 保留原有的notes路由（如有业务需要）
    path('notes/', views.index, name='notes_list'),
]