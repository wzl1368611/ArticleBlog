import time

import requests
from bs4 import BeautifulSoup
import os, re
import sqlite3

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/83.0.4103.97 Safari/537.36 ",

}
# url = 'https://www.duwenzhang.com/wenzhang/shenghuosuibi/shenghuoganwu/20200513/415299.html'
real_url = 'https://www.duwenzhang.com/'


def ask_rul(url):
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        html = requests.get(url, headers=headers).content.decode('gbk', 'ignore')
        soup = BeautifulSoup(html, 'html.parser')
        authors = soup.select('tr .author a')
        refer = soup.select('tr .author')
        # print('相关信息--------------------', refer[0].get_text())
        time = re.compile('时间：(.*?) 阅读')  # 注意时间格式为日期，不包含时间
        hello = time.findall(refer[0].get_text())[0].split(' ')[0]
        # print('时间    ', hello)
        author = authors[0].get_text()
        # print('作者-----------------------', author)
        contents = soup.select('tr td #wenzhangziti p')
        content = ''
        for item in contents:
            content = content + item.get_text()
        title = soup.select('h1')[0].get_text()
        # print('标题-------------------', title)
        # print('内容-------------------', content)
        description = contents[0].get_text() + contents[1].get_text()
        if len(description) >= 40:
            description = description[0:40]
        # print('描述-------------------', description)
        article = Article(author, hello, title, description, content)
        print('ok----------------------')
        save_data(article)


def ask_all_url(url):
    html = requests.get(url, headers=headers).content.decode('gbk', 'ignore')
    # print(html)
    # file = open('templates/爬虫.html', 'r', encoding='utf-8')
    # read = file.read()
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.prettify())
    lists = soup.select('.daohang a')
    # pattern = re.compile('href="(.*?)"')
    myUrls = []
    for item in lists:
        lower_item = item['href']
        # print(lower_item, type(item), '--------------', sep=' ')
        # data = pattern.findall(item)
        # myUrls.append(data)
        myUrls.append(lower_item)

    # file.close()
    # myUrls.pop(0)
    print(myUrls)
    return myUrls


def get_next_level_url():
    urls = []
    # https: // www.duwenzhang.com / wenzhang / shenghuosuibi /
    # https: // www.duwenzhang.com / wenzhang / shenghuosuibi / list_8_2.html
    # https: // www.duwenzhang.com / wenzhang / shenghuosuibi / list_8_3.html
    # print(url, '--------------------')
    base_url = 'https://www.duwenzhang.com/wenzhang/'
    terms = ['aiqingwenzhang', 'qinqingwenzhang', 'youqingwenzhang', 'shenghuosuibi',
             'xiaoyuanwenzhang',
             'jingdianwenzhang', 'renshengzheli', 'lizhiwenzhang', 'gaoxiaowenzhang',
             'xinqingriji', 'yingyuwenzhang']
    number = [1, 2, 3, 8, 4, 5, 6, 7, 9, 69, 10]
    for i in range(1, 12):
        url = base_url + terms[i - 1] + '/'
        for page in range(1, 11):

            strs = 'list_%d_%d.html' % (number[i - 1], page)
            real_url = url + strs
            print(real_url)
            r = requests.get(real_url, headers=headers)
            if r.status_code == 200:
                html = requests.get(real_url, headers=headers).content.decode('gbk', 'ignore')
                soup = BeautifulSoup(html, 'html.parser')
                # print(soup.prettify())
                data = soup.select('.ulink')
                # print(data)
                mydata = []
                for j in range(len(data)):
                    if j % 2 == 1:
                        mydata.append(data[j])
                # print(mydata)
                for item in mydata:
                    urls.append(item['href'])
    # https: // www.duwenzhang.com / wenzhang / aiqingwenzhang / list_1_2.html
    print(urls, '============================')

    # with open('templates/test2.html', 'r', encoding='utf-8') as file:
    #     html = file.read()
    #     soup = BeautifulSoup(html, 'html.parser')
    #     data = soup.select('.ulink')
    #     # print(data)
    #     mydata = []
    #     for i in range(len(data)):
    #         if i % 2 == 1:
    #             mydata.append(data[i])
    #     # print(mydata)
    #     for item in mydata:
    #         urls.append(item['href'])
    # data = soup.select('.ulink')
    # print(data)
    # mydata = []
    # for i in range(15):
    #     if i % 2 == 0:
    #         mydata.append(data[i])
    # print(mydata)

    return urls


def get_data(url):
    ask_rul(url)


import random


class Article:
    author = ''
    time = ''
    title = ''
    content = ''
    description = ''
    type = 0

    def __init__(self, author, time, title, description, content):
        self.author = author
        self.time = time
        self.title = title
        self.description = description
        self.content = content
        self.type = random.randint(0, 4)


def save_data(article):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    # print(article.content)
    for i in range(6):
        article.content = article.content
        article.type = str(article.type)
        article.time = article.time
        article.title = article.title
        article.description = article.description
        article.author = article.author
    image = 'images/moutain001.jfif'
    tui = '0'
    click = '0'
    #  传入数据的方式，sql 语句 显示错误，需要调整sql语句写入
    sql = 'insert into Article_article(title,author,content,description,time,picture,tui,click,types_id) values ("%s","%s","%s","%s","%s","%s","%s","%s","%s")' % \
          (article.title, article.author, article.content, article.description, article.time, image, tui, click,
           article.type)
    print(sql)
    conn.execute(sql)
    cursor.close()
    conn.commit()
    conn.close()


if __name__ == '__main__':
    # url_lists = ask_all_url(real_url)
    all_detail_url = get_next_level_url()
    for url in all_detail_url:
        time.sleep(0.3)
        try:
            every_url = url
            get_data(every_url)
        except Exception as e:
            print('出现异常了。。。。。。', e)
