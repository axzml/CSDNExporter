# CSDNExporter
## 介绍
CSDN 博客导出工具, 用于将 CSDN 博客导出为 Markdown / PDF 格式. 比较赞的地方在于, 它
不仅支持一篇博文的导出, 还支持将某个类目下的博文批量导出, 以及将导出的多篇博文汇总为
一篇, 以便用于全局搜索, 具体效果可以查看 [导出 CSDN 博客至 Markdown 或 PDF 格式 (近乎完美)](https://blog.csdn.net/Eric_1993/article/details/104772437).


## 使用说明

另外要说明的是:

0. 安装必要的 Python 库, 如 `httpx`, `requests`, `BeautifulSoup`, 直接运行 `pip install -r requirements.txt` 即可;
    - 2024-04-24 更新：`BeautifulSoup` 升级为 `beautifulsoup4`，已在 Ubuntu 和 Windows 系统测试过没啥问题;

1. 为了解析图片链接, 需要安装 [aria2](https://aria2.github.io/), 并保证能在命令行启动;
    - 将软件的安装目录加入到环境变量中即可, 加入后最好重启或刷新终端, 如 Bash、Zsh、Terminal、Powershell 等等，如果运行命令 `aria2c --verison` 不报错，说明成功；

2. 为了转换为 PDF, 需要安装 [Pandoc](https://pandoc.org/)
    - 有同学反映转换 pdf 时，遇到 pandoc 的报错 `pandoc: unrecognized option '--pdf-engine=xelatex'`, 因此还需要安装 xelatex, 具体查阅下 pandoc 的安装说明吧。
        - Ubuntu 上可以使用 `sudo apt-get install texlive-xetex` + `sudo apt install latex-cjk-all` 安装 texlive 相关的内容 (注意 [LaTeX Error: File `ctex.sty' not found
](https://tex.stackexchange.com/questions/687540/latex-error-file-ctex-sty-not-found))
        - Pandoc 使用 `sudo apt-get install pandoc` 安装 
        - 代码中使用了 'Source Code Pro' 字体，是我个人很喜欢的编程字体，可以参考 [Source Code Pro Font](https://askubuntu.com/questions/193072/how-to-use-the-adobe-source-code-pro-font) 中 edwin 的回答，从 [Google Font](https://fonts.google.com/) 获取该字体，并按回答中的方法安装到系统中。当然，如果不想使用该字体，只需要将 `main.py` 中关于 'Source Code Pro' 的两行代码给注释掉即可。


此外, 正如博客标题 [导出 CSDN 博客至 Markdown 或 PDF 格式 (近乎完美)](https://blog.csdn.net/Eric_1993/article/details/104772437) 中说的, "近乎完美",
是因为该博客导出工具还有一些细节没有考虑, 没有需求就没有动力去改代码, 精力有限, 目前该工具让我满意 😂😂😂.


## 运行脚本
- Linux系统运行
启动脚本为 `./run.sh`, 使用 `chmod +x run.sh` 增加其可执行权限;
- Windows系统启动
启动脚本为`run.bat`, 双击打开或者在cmd中运行`run.bat`

## 更新历史

+ 2024-04-26: 增加对表格解析的支持
+ 2024-04-25: 修复 Windows 下使用绝对路径报错的问题


## 特别感谢

因个人原因，仓库疏于维护，非常感谢社区成员的关注与支持，尤其感谢如下成员的付出：

[@yaunsine](https://github.com/yaunsine), [@Tim-Saijun](https://github.com/Tim-Saijun), [@66my](https://github.com/66my)
