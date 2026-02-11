from django.db import models
from django.core.exceptions import ValidationError

# ======================== 知识点模型（含自关联） ========================
class Tag(models.Model):
    """知识点模型，支持自关联实现层级分类（如Python > 列表推导式）"""
    name = models.CharField(
        max_length=50,
        verbose_name="知识点名称",
        unique=True  # 确保知识点名称不重复
    )
    # 自关联字段：实现知识点的父子层级关系
    parent = models.ForeignKey(
        "self",  # 关联模型为自身
        on_delete=models.SET_NULL,  # 父知识点删除时，子知识点的parent字段设为NULL
        null=True,
        blank=True,
        related_name="children",  # 反向查询：父知识点查子知识点（parent_tag.children.all()）
        verbose_name="父知识点"
    )

    def __str__(self):
        """友好显示：带层级关系（如“Python > 列表推导式”）"""
        if self.parent:
            return f"{self.parent.name} > {self.name}"
        return self.name

    def clean(self):
        """核心验证：禁止自关联循环（如A→B→A）"""
        current = self
        # 循环遍历父级链条，检查是否指向自身
        while current.parent:
            if current.parent == self:
                raise ValidationError("❌ 禁止循环关联！不能将自身/子知识点设为父知识点")
            current = current.parent

    def save(self, *args, **kwargs):
        """保存前强制触发验证，确保无循环关联"""
        self.full_clean()  # 调用clean()方法做验证
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "知识点"
        verbose_name_plural = "知识点"  # 后台显示复数名称
        ordering = ["name"]  # 按名称升序排列

# ======================== 错题模型（多对多关联知识点） ========================
class ErrorNote(models.Model):
    """错题模型，与知识点为多对多关联"""
    title = models.CharField(max_length=100, verbose_name="错题标题")
    content = models.TextField(verbose_name="题目内容")
    my_answer = models.CharField(max_length=200, verbose_name="我的答案")
    correct_answer = models.CharField(max_length=200, verbose_name="正确答案")
    analysis = models.TextField(verbose_name="错题解析")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")  # 自动记录创建时间
    # 多对多关联知识点：一道错题可关联多个知识点，一个知识点可对应多道错题
    tags = models.ManyToManyField(
        Tag,
        related_name="error_notes",  # 反向查询：知识点查错题（tag.error_notes.all()）
        verbose_name="关联知识点"
    )

    def __str__(self):
        """友好显示：显示错题标题"""
        return self.title

    class Meta:
        verbose_name = "错题"
        verbose_name_plural = "错题"
        ordering = ["-create_at"]  # 按创建时间倒序（最新的错题在前面）

# ======================== 操作日志模型（外键关联错题） ========================
class OperationLog(models.Model):
    """操作日志模型，记录错题的新增/编辑/删除/关联知识点等操作"""
    # 操作类型：固定可选值，避免随意输入
    OPERATE_CHOICES = [
        ("add", "新增错题"),
        ("edit", "编辑错题"),
        ("delete", "删除错题"),
        ("bind_tag", "关联知识点"),
        ("unbind_tag", "取消关联知识点")
    ]
    operate_type = models.CharField(
        max_length=20,
        verbose_name="操作类型",
        choices=OPERATE_CHOICES
    )
    content = models.CharField(
        max_length=200,
        verbose_name="操作内容",
        help_text="如：新增错题“列表推导式语法错误”"  # 后台输入提示
    )
    operate_time = models.DateTimeField(auto_now_add=True, verbose_name="操作时间")
    # 外键关联错题：删除错题时，关联的日志也同步删除（级联删除）
    related_error = models.ForeignKey(
        ErrorNote,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="关联错题"
    )

    def __str__(self):
        """友好显示：时间 + 操作类型 + 内容"""
        return f"{self.operate_time.strftime('%Y-%m-%d %H:%M')} | {self.get_operate_type_display()} | {self.content}"

    class Meta:
        verbose_name = "操作日志"
        verbose_name_plural = "操作日志"
        ordering = ["-operate_time"]  # 按操作时间倒序