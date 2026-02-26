from django.contrib import admin
from .models import Tag, Article

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'created_at']
    filter_horizontal = ['tags']