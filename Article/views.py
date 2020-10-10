from django.shortcuts import render, HttpResponse
from Article.models import *
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    first_10 = Article.objects.order_by('-time')[:10]  # 取前10条
    tui_7 = Article.objects.filter(tui=1).order_by('-time')[:7]  # 取前10条
    click_12 = Article.objects.order_by('-click')[:12]
    return render(request, 'index.html', locals())


def lists(request, id):
    id = int(id)
    page_number = request.GET.get('page', 1)  # 获得get请求的对象
    types = Type.objects.get(id=id)
    articles = types.article_set.order_by('-time')  # 一查询多的方式
    p = Paginator(articles, 10)
    page = p.page(int(page_number))
    return render(request, 'lists.html', locals())


def picture(request):
    return render(request, 'picture.html')


def article(request, id):
    id = int(id)
    articles = Article.objects.get(id=id)

    return render(request, 'article.html', locals())

# from Article.models import Type, Article
# import datetime

# def addArticle(request):
#     for i in range(100):
#         a = Article()
#         if i % 4 == 1:
#             a.title = '散文_%s' % i
#             a.types = Type.objects.get(id=1)
#             a.description = '这是一篇散文'
#             a.content = '这是一篇散文 这是一篇散文 这是一篇散文 /n' * 10
#         elif i % 4 == 2:
#             a.title = '小说_%s' % i
#             a.types = Type.objects.get(id=2)
#             a.description = '这是一篇小说'
#             a.content = '这是一篇小说 这是一篇小说 这是一篇小说 /n' * 10
#         elif i % 4 == 3:
#             a.title = '技术文章_%s' % i
#             a.types = Type.objects.get(id=3)
#             a.description = '这是一篇技术文章'
#             a.content = '这是一篇技术文章 这是一篇技术文章 这是一篇技术文章 /n' * 10
#         else:
#             a.title = '日记_%s' % i
#             a.types = Type.objects.get(id=4)
#             a.description = '这是一篇日记'
#             a.content = '这是一篇日记 这是一篇日记 这是一篇日记 /n' * 10
#
#         a.tui = 0
#         a.click = 0
#         a.picture = 'images/666.jpg'
#         a.time = datetime.datetime.now()
#         a.save()
#     return HttpResponse('保存成功')
# title = models.CharField(max_length=32)
# author = models.CharField(max_length=32)
# content = RichTextField()
# description = RichTextField()
# time = models.DateField()
# picture = models.ImageField(upload_to='images')
# tui = models.IntegerField()  # 0代表不推荐  1 安代表表推荐
# click = models.IntegerField()  # 点击加1
# types = models.ForeignKey(to=Type, null=True, on_delete=models.SET_NULL)  # 外键
