# 初始化脚本：知识点/错误类型数据
import os
import django

# 配置Django环境（必须）
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eb_project.settings')
django.setup()

# 导入模型
from error_notes.models import Tag


def init_tags():
    """初始化知识点/错误类型数据"""
    # 预设的知识点数据（层级结构）
    tag_data = [
        # 顶级知识点（父知识点为None）
        {"name": "Python", "parent": None},
        {"name": "MySQL", "parent": None},
        {"name": "Django", "parent": None},
        # 子知识点（父知识点为对应顶级标签）
        {"name": "列表推导式", "parent": "Python"},
        {"name": "装饰器", "parent": "Python"},
        {"name": "索引优化", "parent": "MySQL"},
        {"name": "模型迁移", "parent": "Django"},
        # 错误类型（单独分类）
        {"name": "语法错误", "parent": None},
        {"name": "逻辑错误", "parent": None},
        {"name": "数据库错误", "parent": None},
    ]

    # 批量插入/更新数据（避免重复）
    for item in tag_data:
        # 查找父知识点
        parent_tag = None
        if item["parent"]:
            parent_tag = Tag.objects.filter(name=item["parent"]).first()

        # 用get_or_create避免重复插入
        Tag.objects.get_or_create(
            name=item["name"],
            defaults={"parent": parent_tag}
        )
        print(f"✅ 初始化知识点：{item['name']}（父：{item['parent']}）")


if __name__ == "__main__":
    print("开始初始化知识点/错误类型数据...")
    init_tags()
    print("🎉 知识点/错误类型初始化完成！")