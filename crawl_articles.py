# -*- coding: utf-8 -*-

import wechatsogou
import requests
import re
import os
from py_mysql import *
import MySQLdb
from urllib.parse import quote
from bs4 import BeautifulSoup

mysql_client = MysqlClient()

#获取微信文章页面文字内容，以便直接搜索
def parse_content_by_url(url):
    if url is None:
            return
    html = requests.get(url)
    orgin_source = html.text
    soup = BeautifulSoup(orgin_source, 'html.parser')
    try:
        content = soup.find('div', class_='rich_media_content ').get_text()#文章内容
        return content
    except Exception:
        return None

# 获取url页面的html源码，并替换图片源址
# TODO,优化存储html代码，仅存储部分 doc = pq(fix_doc)('#js_content')
def parse_html_by_url(url):
    if url is None:
            return
    html = requests.get(url)
    orgin_source = html.text
    try:
        fix_html = re.sub('data-src', 'src', orgin_source)
        return fix_html
    except Exception:
        return None


#存储文章到本地
def save_content_file(title,content):
    with open(title,'w') as f:
        f.write(content)

#创建公众号命名的文件夹
def create_dir(keywords):
    if not os.path.exists(keywords):
        os.makedirs(keywords)

#解析历史文章,并保存到公众号文件夹下
def parse_articles(keywords):
    ws_api = wechatsogou.WechatSogouAPI()
    gzh_articles = ws_api.get_gzh_artilce_by_history(keywords)
    gzh_info = list(gzh_articles)[0]
    wechat_info = gzh_articles[gzh_info]
    wechat_id = wechat_info['wechat_id']
    wechat_name = wechat_info['wechat_name']
    articles = list(gzh_articles)[1]
    temp_content = gzh_articles[articles]
    for i in range(10):
        article_dict = temp_content[i]
        send_id = article_dict['send_id']
        field_id = article_dict['fileid']
        msg_type = article_dict['type']
        artcile_type = article_dict['copyright_stat']
        main = article_dict['main']
        released_time = article_dict['datetime']
        title = article_dict['title']
        author = article_dict['author']
        abstract = article_dict['abstract']
        url = article_dict['content_url']
        cover = article_dict['cover']
        content = parse_content_by_url(url)
        html = parse_html_by_url(url)
        contentfiletitle = keywords + '/' + article_dict['title'] + '_' + str(article_dict['datetime']) + '.html'
        save_content_file(contentfiletitle,html)
        try:
            print('ready for save to mysql')
            sql = "INSERT INTO article(field_id,send_id,msg_type,artcile_type,main,released_time, \
                    wechat_id,wechat_name,title,author,abstract,url,cover,content,html ) values \
                    ({},{},{},{},{},{},'{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(field_id, \
                    send_id,msg_type,artcile_type,main,released_time, \
                    wechat_id,wechat_name,title,author,abstract,url,cover,content,\
                    quote(html))
            print(sql)
            mysql_client.query(sql)
            print('data saved')
        except:
            print('exception 存储错误')

def main():
    prompt = 'Please input wechat name:'
    gzh = input(prompt)
    create_dir(gzh)
    if not gzh:
        print('say sth！')
    parse_articles(gzh)


if __name__ == '__main__':
    main()
