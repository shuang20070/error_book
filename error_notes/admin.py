from django.contrib import admin
# 导入所有模型（知识点、错题、操作日志）
from .models import Tag, ErrorNote, OperationLog

# ======================== 知识点（Tag）后台配置 ========================
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """知识点后台管理配置"""
    # 列表页显示的字段（含自关联的parent字段）
    list_display = ["id", "name", "parent"]
    # 搜索框：按知识点名称搜索
    search_fields = ["name"]
    # 筛选器：按父知识点筛选（快速找某类子知识点）
    list_filter = ["parent"]
    # 编辑页字段排序
    fields = ["name", "parent"]
    # 只读字段（可选，如需保护id等字段）
    readonly_fields = ["id"]
    # 列表页可直接编辑的字段（无需进入详情页）
    list_editable = ["parent"]

# ======================== 错题（ErrorNote）后台配置 ========================
@admin.register(ErrorNote)
class ErrorNoteAdmin(admin.ModelAdmin):
    """错题后台管理配置，优化多对多字段体验"""
    # 列表页显示的核心字段
    list_display = ["id", "title", "create_at", "tag_names"]
    # 搜索框：按标题、题目内容、解析搜索
    search_fields = ["title", "content", "analysis"]
    # 筛选器：按创建时间、关联知识点筛选
    list_filter = ["create_at", "tags"]
    # 编辑页字段分组（优化长表单体验）
    fieldsets = (
        ("错题基本信息", {
            "fields": ("title", "content", "my_answer", "correct_answer", "analysis")
        }),
        ("关联信息", {
            "fields": ("tags",),
            "description": "按住Ctrl键可多选知识点"  # 友好提示
        }),
    )
    # 多对多字段使用横向选择框（比默认下拉框更易用）
    filter_horizontal = ["tags"]
    # 只读字段（创建时间自动生成，禁止手动修改）
    readonly_fields = ["id", "create_at"]
    # 列表页排序（默认按创建时间倒序）
    ordering = ["-create_at"]

    def tag_names(self, obj):
        """自定义列表字段：显示关联的知识点名称（逗号分隔）"""
        return ", ".join([tag.name for tag in obj.tags.all()])
    # 自定义字段的友好名称
    tag_names.short_description = "关联知识点"

# ======================== 操作日志（OperationLog）后台配置 ========================
@admin.register(OperationLog)
class OperationLogAdmin(admin.ModelAdmin):
    """操作日志后台管理配置"""
    # 列表页显示的核心字段
    list_display = ["id", "operate_time", "operate_type", "content", "related_error_title"]
    # 搜索框：按操作内容、关联错题标题搜索
    search_fields = ["content", "related_error__title"]
    # 筛选器：按操作类型、操作时间筛选
    list_filter = ["operate_type", "operate_time"]
    # 日志为只读（禁止修改，确保操作记录真实）
    readonly_fields = ["id", "operate_time", "operate_type", "content", "related_error"]
    # 编辑页禁用（日志只能通过代码自动生成，不允许手动添加）
    def has_add_permission(self, request):
        return False
    # 禁止删除日志（保留完整操作记录）
    def has_delete_permission(self, request, obj=None):
        return False
    # 列表页排序（按操作时间倒序）
    ordering = ["-operate_time"]

    def related_error_title(self, obj):
        """自定义列表字段：显示关联错题的标题（无关联则显示“无”）"""
        return obj.related_error.title if obj.related_error else "无"
    # 自定义字段的友好名称
    related_error_title.short_description = "关联错题"