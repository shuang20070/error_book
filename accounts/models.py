from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# 扩展 Django 自带的用户模型
class User(AbstractUser):
    # 新增字段：用户昵称
    nickname = models.CharField(max_length=50, blank=True, verbose_name='昵称')
    # 新增字段：个人简介
    bio = models.TextField(max_length=500, blank=True, verbose_name='个人简介')
    # 新增字段：头像
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name='头像')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def __str__(self):
        return self.username