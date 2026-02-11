# Django ORM & 数据库迁移 核心笔记
## 一、数据库迁移（Migrations）
### 1. 核心命令
| 命令 | 作用 | 适用场景 |
|------|------|----------|
| `python manage.py makemigrations` | 生成迁移文件 | 模型新增/修改/删除后 |
| `python manage.py migrate` | 执行迁移（同步数据库） | 生成迁移文件后 |
| `python manage.py showmigrations` | 查看迁移执行状态 | 验证迁移是否全部执行 |
| `python manage.py migrate --fake` | 标记迁移为已执行（不修改数据库） | 数据库和迁移文件不一致时 |

### 2. 迁移原理
- 迁移文件保存在各app的`migrations`文件夹，记录模型结构的变更；
- 每次`migrate`会对比迁移文件和数据库`django_migrations`表，只执行未执行的迁移。

### 3. 常见问题
- 迁移冲突：删除冲突的迁移文件+数据库中对应记录，重新`makemigrations`；
- 字段重命名：需先`makemigrations`，再手动修改迁移文件中的`rename_field`。

## 二、ORM核心操作（CRUD）
### 1. 基础查询
- 查询所有：`Model.objects.all()`
- 条件查询：`Model.objects.filter(字段=值)`
- 单个查询：`Model.objects.get(id=1)`（无结果/多结果会报错）
- 模糊查询：`Model.objects.filter(name__contains="Python")`
- 关联查询：`Tag.objects.filter(parent__name="Python")`（子查父）

### 2. 新增数据
- 快捷方式：`Model.objects.create(字段1=值1, 字段2=值2)`
- 实例化方式：
  ```python
  obj = Model(字段1=值1)
  obj.save()
  obj = Model.objects.get(id=1)
obj.name = "新名称"
obj.save()
## 三、数据验证器
### 1. 自定义验证器
- 函数式验证器：定义函数+在模型字段`validators`中引用；
- 核心验证场景：非空、长度限制、特殊字符过滤、循环关联检测。

### 2. 验证器触发方式（三种核心场景）
| 触发方式 | 操作步骤 | 适用场景 |
|----------|----------|----------|
| `obj.full_clean()` | 1. Shell中创建模型实例<br>2. 调用`obj.full_clean()`<br>3. 捕获ValidationError异常 | 开发调试，手动验证单个对象 |
| 后台页面保存 | 1. 启动服务器：`python manage.py runserver`<br>2. 登录后台：http://127.0.0.1:8000/admin/<br>3. 输入非法数据，点击保存 | 测试生产环境，直观看到报错提示 |
| `form.is_valid()` | 1. 创建ModelForm表单类<br>2. 传入数据初始化表单<br>3. 调用`form.is_valid()` | 前端提交数据，验证表单+模型字段 |

#### 示例代码（Shell触发）
```python
from error_notes.models import Tag
from django.core.exceptions import ValidationError

# 测试空名称验证
tag_empty = Tag(name="", parent=None)
try:
    tag_empty.full_clean()  # 手动触发验证
except ValidationError as e:
    print("验证报错：", e.message_dict['name'][0])  # 输出：知识点名称不能为空！
from django import forms
from .models import Tag

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'parent']

# 测试非法数据
invalid_data = {'name': '', 'parent': None}
form = TagForm(data=invalid_data)
print(form.is_valid())  # 输出False
print(form.errors)      # 输出：{'name': ['知识点名称不能为空！']}
from django import forms
from .models import Tag

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'parent']

# 测试非法数据
invalid_data = {'name': '', 'parent': None}
form = TagForm(data=invalid_data)
print(form.is_valid())  # 输出False
print(form.errors)      # 输出：{'name': ['知识点名称不能为空！']}

## 步骤3：保存文件
### 方式1：记事本保存
- 按 `Ctrl+S` 快捷键保存；
- 关闭记事本，重新打开确认内容已更新。

### 方式2：PyCharm保存
- 按 `Ctrl+S` 快捷键；
- 或点击右上角「保存」图标（💾）；
- 确认文件内容中包含：
  ✅ 三种验证器触发方式的表格+示例代码；
  ✅ 删除报错的原因+解决方法；
  ✅ 格式清晰，无乱码。

## 最终验证
打开 `django_orm_migrations_notes.md` 文件，检查以下内容是否存在：
1. `obj.full_clean()`、后台保存、`form.is_valid()` 三种触发方式的详细说明；
2. 删除报错的原因（id为None）和解决方法（先save再delete）；
3. 完整的示例代码片段。

补充完成后，你的ORM/迁移知识点笔记就涵盖了**核心操作+验证逻辑+常见问题**，内容完整且实用，接下来就可以继续推进“完善项目框架+提交GitHub”的任务啦～

如果需要我帮你检查笔记内容是否完整，或者整理提交GitHub的最终步骤，都可以告诉我！