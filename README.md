# Django 错题本管理系统

> 一个基于 Django 框架开发的错题本管理系统，支持错题录入、分类、检索、CRUD 操作及后台管理，帮助用户高效整理和复习学习中的错题。

## 功能特性 ✨

- **错题管理**：支持错题的增、删、改、查（CRUD）操作
- **分类管理**：按科目、知识点对错题进行分类
- **数据验证**：完善的表单验证机制，保证数据合法性
- **后台管理**：通过 Django Admin 快速管理所有数据
- **响应式界面**：适配不同设备的前端展示

## 技术栈 🛠️

- **后端**：Django 4.x
- **数据库**：SQLite（开发环境）/ MySQL（生产环境）
- **前端**：HTML5 + CSS3 + JavaScript
- **版本控制**：Git + GitHub

## 快速开始 🚀

### 1. 克隆项目
```bash
git clone https://github.com/shuang20070/error_book.git
cd error_book
```

### 2. 创建并激活虚拟环境
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. 安装依赖
```bash
pip install -r requirements.txt
```

### 4. 数据库迁移
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. 创建超级用户（用于后台管理）
```bash
python manage.py createsuperuser
```

### 6. 启动开发服务器
```bash
python manage.py runserver
```

访问 http://127.0.0.1:8000 即可使用系统，访问 http://127.0.0.1:8000/admin 进入后台管理。

## 项目结构 📁

```
error_book/
├── accounts/          # 用户账户相关应用
├── docs/              # 项目文档
├── eb_project/        # 项目主配置目录
├── error_notes/       # 错题核心应用
├── scripts/           # 辅助脚本
├── templates/         # 模板文件
├── manage.py          # Django 管理脚本
├── .gitignore         # Git 忽略文件配置
└── README.md          # 项目说明文档
```

## 后续开发建议 💡

1. **功能扩展**：可添加错题统计分析、错题导出为 PDF 等功能
2. **部署上线**：可部署到阿里云、腾讯云或 Heroku 等平台
3. **前端优化**：引入 Vue/React 等前端框架提升用户体验

---
