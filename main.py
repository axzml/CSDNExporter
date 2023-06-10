#############################
# CopyRight ~~~~~~
# Author: axzml
# Date: 2020-03-07
#############################
import os
import sys
import shutil
from os.path import join, exists
import urllib.request
import requests
import httpx
import argparse
import glob
from bs4 import BeautifulSoup, NavigableString
from utils import Parser
import re


parser = argparse.ArgumentParser('CSDN Blog Exporter: To Markdown or To PDF')
group = parser.add_mutually_exclusive_group()
group.add_argument('--category_url', type=str,
                    help='CSDN Category Url, e.g., https://blog.csdn.net/Eric_1993/category_9545994.html')
group.add_argument('--article_url', type=str,
                    help='CSDN Article Url, e.g., https://blog.csdn.net/Eric_1993/article/details/104750599')
parser.add_argument('--start_page', type=int, default=1,
                   help='Start Page of CSDN Category')
parser.add_argument('--page_num', type=int, default=100,
                    help='Page Number of CSDN Category.'
                    ' If you set this to a large number, all articles in all pages of this category will be downloaded')
parser.add_argument('--markdown_dir', type=str, default='markdown',
                   help='Markdown Directory')
parser.add_argument('--pdf_dir', type=str, default='pdf',
                   help='PDF Directory')
# parser.add_argument('--figure_dir', type=str, default='figures',
                   # help='Figures Directory')
parser.add_argument('--with_title', action='store_true')
parser.add_argument('--to_pdf', action='store_true')
parser.add_argument('--rm_cache', action='store_true',
                   help='remove cached file')
parser.add_argument('--is_win', 
                    choices=[1, 0], default=0, type=int,
                   help='platform: windows-1, Linux-0')
parser.add_argument('--combine_together', action='store_true',
                   help='Combine all markdown file in markdown_dir to a single file.'
                   ' And if to_pdf, the single file will be converted pdf format')
args = parser.parse_args()

def html2md(url, md_file, with_title=False, is_win=False):
    response = httpx.get(url)
    soup = BeautifulSoup(response.content, 'html.parser', from_encoding="utf-8")
    html = ""
    for child in soup.find_all('svg'):
        child.extract()
    if with_title:
        for c in soup.find_all('div', {'class': 'article-title-box'}):
            html += str(c)
    for c in soup.find_all('div', {'id': 'content_views'}):
        html += str(c)
    parser = Parser(html, is_win)
    with open(md_file, 'w', encoding="utf-8") as f:
        f.write('{}\n'.format(''.join(parser.outputs)))

def generate_pdf(input_md_file, pdf_dir, is_win=False):
    if not exists(pdf_dir):
        os.makedirs(pdf_dir)

    md_name = os.path.basename(input_md_file)
    pdf_name = md_name.replace('.md', '.pdf')
    pdf_file = join(pdf_dir, pdf_name)
    if is_win:
        cmd = ['pandoc',
            '--toc',
            '--pdf-engine=xelatex',
            '-V mainfont="Source Code Pro"',
            '-V monofont="Source Code Pro"',
            '-V documentclass="ctexbook"',
            '-V geometry:"top=2cm, bottom=1cm, left=1.5cm, right=1.5cm"',
            '-V pagestyle=plain',
            '-V fontsize=11pt',
            '-V colorlinks=blue',
            '-s {}'.format(input_md_file),
            '-o {}'.format(pdf_file),
        ]
    else:
        cmd = ["pandoc",
            "--toc",
            "--pdf-engine=xelatex",
            "-V mainfont='Source Code Pro'",
            "-V monofont='Source Code Pro'",
            "-V documentclass='ctexart'",
            "-V geometry:'top=2cm, bottom=1cm, left=1.5cm, right=1.5cm'",
            "-V pagestyle=plain",
            "-V fontsize=11pt",
            "-V colorlinks=blue",
            "-s {}".format(input_md_file),
            "-o {}".format(pdf_file),
        ]
    cmd = ' '.join(cmd)
    print('Generate PDF File: {}'.format(pdf_file))
    os.system(cmd)

def get_category_article_info(soup):
    url = soup.find_all('a')[0].attrs['href']
    h2_tag = soup.find_all('h2', {'class': 'title'})[0]
    for child in h2_tag.children:
        if isinstance(child, NavigableString):
            title = '_'.join(child.replace('*', '').strip().split())
            break
    return url, title

def download_csdn_category_url(category_url, md_dir, start_page=1, page_num=100, pdf_dir='pdf', to_pdf=False, is_win=False):
    """
    如果想下载某个 category 下的所有页面, 那么 page_num 设置大一些
    """
    if not exists(md_dir):
        os.makedirs(md_dir)

    article_url = []
    article_title = []
    for page in range(start_page, page_num + 1):
        suffix = '.html' if page == 1 else '_{}.html'.format(page)
        category_url_new = category_url.rstrip('.html') + suffix
        print('Getting Response From {}'.format(category_url_new))
        response = httpx.get(category_url_new)
        soup = BeautifulSoup(response.content, 'html.parser', from_encoding="utf-8")
        article_list = soup.find_all('ul', {'class': 'column_article_list'})[0]
        p = article_list.find_all('p')
        if p and p[0].string == '空空如也':
            print('No Content in {}, I Will Skip It!'.format(category_url_new))
            break
        for child in article_list.children:
            # if child.name == 'div': # and child.attrs['class'] == 'pagination-box': print(child)
            if child.name == 'li':
                url, title = get_category_article_info(child)
                title = re.compile(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])").sub('', title)
                article_url.append(url)
                article_title.append(title)

    for idx, (url, title) in enumerate(zip(article_url, article_title), 1):
        md_file = join(md_dir, title + '.md')
        print('BlogNum: {}, Exporting Markdown File To {}'.format(idx, md_file))
        if not exists(md_file):
            html2md(url, md_file)
            if to_pdf:
                generate_pdf(md_file, pdf_dir, is_win)


def download_csdn_single_page(details_url, md_dir, with_title=True, pdf_dir='pdf', to_pdf=False, is_win=False):
    if not exists(md_dir):
        os.makedirs(md_dir)
    response = httpx.get(details_url)
    soup = BeautifulSoup(response.content, 'html.parser', from_encoding="utf-8")
    title = soup.find_all('h1', {'class': 'title-article'})[0].string  ## 使用 html 的 title 作为 md 文件名
    title = '_'.join(title.replace('*', '').strip().split())
    md_file = join(md_dir, title + '.md')
    print('Export Markdown File To {}'.format(md_file))
    html2md(details_url, md_file, with_title=with_title, is_win=is_win)
    if to_pdf:
        generate_pdf(md_file, pdf_dir, is_win)


if __name__ == '__main__':
    if not args.category_url and not args.article_url:
        raise Exception('Option category_url or article_url is not specified!')

    if exists(args.markdown_dir) and args.rm_cache:
        shutil.rmtree(args.markdown_dir)

    if exists('./figures') and args.rm_cache:
        shutil.rmtree('./figures')

    if exists(args.pdf_dir) and args.rm_cache:
        shutil.rmtree(args.pdf_dir)

    if args.category_url:
        download_csdn_category_url(args.category_url,
                                   args.markdown_dir,
                                   start_page=args.start_page,
                                   page_num=args.page_num,
                                   pdf_dir=args.pdf_dir,
                                   to_pdf=args.to_pdf)
    else:
        download_csdn_single_page(args.article_url,
                                 args.markdown_dir,
                                 with_title=args.with_title,
                                 pdf_dir=args.pdf_dir,
                                 to_pdf=args.to_pdf)
    is_win = args.is_win == 1
    if args.combine_together:
        source_files = join(args.markdown_dir, '*.md')
        md_file = 'my_together_file.md'  ## 当我清醒过来之后才发现取了一个这样的名字
        if is_win:
            cmd_line = f"type {source_files} > {md_file}"
        else:
            cmd_line = 'cat {} > {}'.format(source_files, md_file)
        os.system(cmd_line)
        if args.to_pdf:
            generate_pdf(md_file, args.pdf_dir, is_win)

