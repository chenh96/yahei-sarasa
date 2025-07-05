# 介绍

本项目代码原用于，将更纱黑体的信息改为微软雅黑和宋体的，来替换 Windows 系统的默认字体。

现在改为，通过更纱黑体的源码，将思源黑体和 Segoe UI 结合为微软雅黑和宋体。

该字体主要是使用了更纱黑体的 Hint 机制，能够提供更锐利的显示效果。

# 构建流程

1. 参考原版微软雅黑，移除 Segoe UI 中大多数 OpenType 特性；

2. 将 Segoe UI 伪装成 Inter 字体，替换更纱黑体项目的源字体；

3. 修改更纱黑体源码，保留 Segoe UI 中的 Hinting；

4. 执行更纱黑体的构建流程，得到构建出的更纱黑体；

5. 修改更纱黑体字体信息，伪装成微软雅黑和宋体。

# 接下来

1. 编写更加自动化的代码，而不是靠手搓；

2. 能够实现输入任意中文字体和拉丁字体，构建出包含 Hinting 的合成字体。


# DIY

如果你想要自行构建字体，那么请参阅以下内容：

## 简单构建

本流程将介绍如何直接将更纱黑体伪装成微软雅黑。

需要你安装 Python 依赖：`fonttools`

你可以在 `rename_ttf.py` 中修改构建配置。

1. 在本项目目录下创建目录 `temp/`，将更纱黑体放置至此目录下；

2. 执行 `python3 rename_ttf.py`，结果会输出至项目目录的 `result/` 目录下。

## 使用 Segoe UI 作为英文字体构建

本流程将介绍，中文使用思源黑体而英文使用 Segoe UI 时该如何自行构建。

需要你安装 FontForge 程序并配置好 Python 开发环境。需要你安装 Python 依赖：`fonttools`

你可以在 `rename_segoe.py`、`rename_ttf.py` 中修改构建配置。

1. 在本项目目录下创建目录 `segoe/`，将 Segoe UI 放置至此目录下；

2. 前往 [Inter](https://github.com/rsms/inter) 下载字体，放置至项目目录的 `inter/` 目录下;

3. 执行 `python3 rename_segoe.py`，中间字体会输出至项目目录的 `temp/` 目录下;

4. 前往 [更纱黑体](https://github.com/be5invis/Sarasa-Gothic) 拉取项目；

5. 参考本项目的文件 `config.json.ui` 来配置更纱黑体的构建配置；

6. 【可选】修改更纱黑体项目的 `verdafile.mjs` 文件，移除运行 `ttfautohint` 的代码；

7. 将【3】生成的 Inter 字体放置至更纱黑体项目的 `sources/Inter` 目录下；

8. 按照更纱黑体的项目说明，构建更纱黑体；

7. 将更纱黑体项目的 `out/TTF/` 目录下的文件放置至本项目的 `temp/` 目录下，并参考【简单构建】得到微软雅黑。
