from django.contrib import admin
from Article.models import Article, Type, Picture


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'time']


class TypeAdmin(admin.ModelAdmin):
    list_display = ['name']


class PictureAdmin(admin.ModelAdmin):
    list_display = ['label', 'description']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Picture, PictureAdmin)
