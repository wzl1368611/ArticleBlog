# ArticleBlog
个人博客

这是一个django框架写的简易的个人博客展示，内容为网上下载的文章

1.spider利用BeautifulSoup进行数据解析，得出文章的内容相关信息，存储到数据库中

2.利用models.py生成db.sqlite数据库文件，分别为Article_type、Article_article、Article_picture表

3.使用了ckeditor富文本编辑器，可以所见即所得的传入文章

4.利用admin来管理数据、添加内容，博客展现内容美观、精彩

