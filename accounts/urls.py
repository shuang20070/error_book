from django.urls import path
from . import views

urlpatterns = [
    # 后续我们会在这里添加注册、登录等路由
]
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]