# wulicode-api-testing

介绍： 这是一个基于 [Seldom](https://github.com/SeldomQA/seldom) 测试框架实现的接口自动化项目。

### 安装

```shell
pip install -r requirements.txt
```

### 目录结构

```
project/
.
├── __init__.py
├── run.py   # 运行用例入口文件
├── quick_public  # 封装公共调用
│   ├── __init__.py
│   ├── module
│   │   ├── __init__.py
│   │   └── module_v1.py  # v1 通过版本号减少后续兼容问题
│   ├── project
│   │   ├── __init__.py
│   │   └── project_v1.py
│   └── 2-system
│       ├── __init__.py
│       └── user_login.py
├── reports   # 测试报告&日志目录
│   ├── 2022_05_18_12_05_04_result.html
│   └── seldom_log.log
├── assets  # 测试数据目录
│   ├── __init__.py  # 存放通用的测试数据
│   └── json_data.json  # 具体用例的数据驱动文件
└── test_dir   # 测试用例目录
    ├── __init__.py
    ├── test_case   # 按照功能模块划分
    │   ├── __init__.py
    │   ├── test_case_create.py
    │   └── test_case_query.py
    ├── test_module
    │   ├── __init__.py
    │   └── test_module_query.py
    ├── test_project
    │   ├── __init__.py
    │   └── test_project_query.py
    └── test_user
        ├── __init__.py
        └── test_access.py
```

### 运行

```
seldom -r run.py
```

带有辅助数据的不能进行单独运行, 必须依托于 Class

### 相关文档

- [Requests](https://requests.readthedocs.io/en/latest/api/)
- [Seldom](https://github.com/SeldomQA/seldom) 