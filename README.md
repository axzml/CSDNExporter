# CSDNExporter

CSDN 博客导出工具, 用于将 CSDN 博客导出为 Markdown / PDF 格式. 比较赞的地方在于, 它
不仅支持一篇博文的导出, 还支持将某个类目下的博文批量导出, 以及将导出的多篇博文汇总为
一篇, 以便用于全局搜索, 具体效果可以查看 [导出 CSDN 博客至 Markdown 或 PDF 格式 (近乎完美)](https://blog.csdn.net/Eric_1993/article/details/104772437).

启动脚本为 `./run.sh`, 使用 `chmod +x run.sh` 增加其可执行权限;

另外要说明的是:

0. 安装必要的 Python 库, 如 `httpx`, `requests`, `BeautifulSoup`;
1. 为了解析图片链接, 需要安装 [aria2](https://aria2.github.io/), 并保证能在命令行启动;
2. 为了转换为 PDF, 需要安装 [Pandoc](https://pandoc.org/)

此外, 正如博客标题 [导出 CSDN 博客至 Markdown 或 PDF 格式 (近乎完美)](https://blog.csdn.net/Eric_1993/article/details/104772437) 中说的, "近乎完美",
是因为该博客导出工具还有一些细节没有考虑, 没有需求就没有动力去改代码, 精力有限, 目前该工具让我满意 😂😂😂.
