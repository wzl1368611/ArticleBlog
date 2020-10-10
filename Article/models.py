from django.db import models
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=32)
    description = RichTextField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=32)
    author = models.CharField(max_length=32)
    content = RichTextField()
    description = RichTextField()
    time = models.DateField()
    picture = models.ImageField(upload_to='images')
    tui = models.IntegerField()  # 0代表不推荐  1 安代表表推荐
    click = models.IntegerField()  # 点击加1
    types = models.ForeignKey(to=Type, null=True, on_delete=models.SET_NULL)  # 外键

    def __str__(self):
        return self.title


class Picture(models.Model):
    image = models.ImageField(upload_to='images')
    label = models.CharField(max_length=32)
    description = RichTextField()

    # def __str__(self):
    #     return self.label
