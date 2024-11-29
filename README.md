# 介绍

本项目主要用于自动将更纱黑体转换为微软雅黑和宋体，它包含以下功能：
- 自动下载并解压最新的更纱黑体发行版
- 使用 fontforge 篡改更纱黑体中的字体信息
- 合并篡改后的文件，把它放到指定目录

# 关于代码的运行

> 建议使用 ubuntu，其他操作系统可能会缺少相关依赖

1. 在 ubuntu 中安装以下依赖
```bash
apt install fontforge
apt install python3-fontforge
```

2. 在 pip 中安装以下依赖
```bash
pip3 install wget
pip3 install py7zr
```

3. 运行入口文件
```bash
python3 auto_all.py
```

# 关于配置

在 `auto_configs.py` 文件中修改生成配置：
```python
HINTED  # 是否下载 Hinted 版本
REGULAR_SOURCE  # 标准字体来源的文件名
BOLD_SOURCE  # 粗体来源的文件名
LIGHT_SOURCE  # 细体来源的文件名
SIMSUN_SOURCE  # 宋体来源的文件名
COPYRIGHT  # 字体的 Copyright
TEMP_DIR  # 临时目录
RESULT_DIR  # 结果目录
OTHER_COPY  # 你想复制的其他文件到结果目录
```

# 或许是更好的选择

最近发现的远景大佬修复版 Noble Scarlet，链接：[PCbeta](https://bbs.pcbeta.com/viewthread-1960120-1-1.html)
