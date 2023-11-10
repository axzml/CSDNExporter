@echo off
@title CSDNExporter
@CHCP 65001
@cls
@color 9F
@echo ================================================================================
@echo ^|^|=================== CSDNExporter（Windows版本） ==========================^|^|
@echo ^|^|============= Github链接：https://github.com/axzml/CSDNExporter ==============^|^|
@echo ================================================================================

set download_category="true"
set category_url="https://blog.csdn.net/hiwangwenbing/category_10280587.html"
set article_url="https://blog.csdn.net/HiWangWenBing/article/details/112058664"
set start_page=1
set page_num=100
set markdown_dir=markdown
set pdf_dir=pdf

if %download_category% == "true" (
    echo "download a category"
    python -u main.py ^
        --category_url %category_url% ^
        --start_page %start_page% ^
        --page_num %page_num% ^
        --markdown_dir %markdown_dir% ^
        --pdf_dir %pdf_dir% ^
        --to_pdf ^
        --is_win 1
        @REM --with_title ^
        @REM --rm_cache
) else (
    echo "download an article"
    python -u main.py ^
        --article_url %article_url% ^
        --markdown_dir %markdown_dir% ^
        --pdf_dir %pdf_dir% ^
        --to_pdf ^
        --with_title ^
        --rm_cache ^
        --is_win 1
)
pause