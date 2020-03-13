#!/bin/bash
#############################
# CopyRight ~~~~~~
# Author: axzml
# Date: 2020-03-07
#############################

set +x
download_category=false  ## 如果为 true, 就需要指定 catetory 的 url; 否则需要指定文章的 url
category_url='https://blog.csdn.net/Eric_1993/category_9545994.html'
article_url='https://blog.csdn.net/eric_1993/article/details/102907104'
start_page=1
page_num=100
markdown_dir='markdown'
pdf_dir='pdf'

if ${download_category}; then
    python -u main.py \
        --category_url ${category_url} \
        --start_page ${start_page} \
        --page_num ${page_num} \
        --markdown_dir ${markdown_dir} \
        --pdf_dir ${pdf_dir} \
        --combine_together \
        --to_pdf \
        #--with_title \
        #--rm_cache \ ## dangerous option, remove all caches
else
    python -u main.py \
        --article_url ${article_url} \
        --markdown_dir ${markdown_dir} \
        --pdf_dir ${pdf_dir} \
        --to_pdf \
        #--with_title \
        #--rm_cache \ ## dangerous option, remove all caches
        #--combine_together \
fi
