# CSDNExporter
## 介绍
CSDN 博客导出工具, 用于将 CSDN 博客导出为 Markdown / PDF 格式. 比较赞的地方在于, 它
不仅支持一篇博文的导出, 还支持将某个类目下的博文批量导出, 以及将导出的多篇博文汇总为
一篇, 以便用于全局搜索, 具体效果可以查看 [导出 CSDN 博客至 Markdown 或 PDF 格式 (近乎完美)](https://blog.csdn.net/Eric_1993/article/details/104772437).

## 运行脚本
- Linux系统运行
启动脚本为 `./run.sh`, 使用 `chmod +x run.sh` 增加其可执行权限;
- Windows系统启动
启动脚本为`run.bat`, 双击打开或者在cmd中运行`run.bat`

## 补充

另外要说明的是:

0. 安装必要的 Python 库, 如 `httpx`, `requests`, `BeautifulSoup`;
1. 为了解析图片链接, 需要安装 [aria2](https://aria2.github.io/), 并保证能在命令行启动;
2. 为了转换为 PDF, 需要安装 [Pandoc](https://pandoc.org/), 同时需要安装[MiKTeX](https://miktex.org/download);
3. 安装字体[Source Code Pro](https://github.com/adobe-fonts/source-code-pro), windows用户建议安装ttf格式; 或修改main.py->generate_pdf方法中'-V mainfont="Source Code Pro"'等字体参数.

99. 下载过快容易被CSDN屏蔽！
100. TODO: 标题没有处理完善！
101. 如MD文件无法正常转换为PDF，可使用VSCODE + Markdown Preview Enhanced插件
(https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced)实现。
使用VSCODE打开MD文件-右键菜单-打开侧边预览-在预览页面打开右键菜单-Open in browser-打印为PDF即可。


此外, 正如博客标题 [导出 CSDN 博客至 Markdown 或 PDF 格式 (近乎完美)](https://blog.csdn.net/Eric_1993/article/details/104772437) 中说的, "近乎完美",
是因为该博客导出工具还有一些细节没有考虑, 没有需求就没有动力去改代码, 精力有限, 目前该工具让我满意 😂😂😂.

#修复记录
20231109
1.在README中增加Pando和MikTex引擎安装信息。
2.修复Windows下`run.bat`中--to_pdf参数未生效的问题。
3.修复文章中存在gif,bmp格式图片时下载失败的问题。
4.修复文章中存在无后缀格式图片下载失败的问题。
5.修复文章中存在匹配图片格式但实际不是图片url导致下载失败的问题。
6.修复generate_pdf方法的is_win参数未生效的问题。
7.修复MD文件中图片路径由于img_file = join(self.fig_dir, img_file)导致未正常转义引发PDF转换失败的问题。

20231110
1.pandoc增加--verbose参数，便于后续调试。