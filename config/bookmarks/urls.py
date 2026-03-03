from django.urls import path
from . import views

url_patterns = [
    path('', views.article_list, name='article_list')
]