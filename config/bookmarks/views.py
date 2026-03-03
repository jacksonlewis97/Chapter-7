from django.shortcuts import render
from .models import Article

def article_list(request):
    articles = Article.objects.prefetch_related('tags').all()
    return render(
        request,
        'bookmarks/article_list.html',
        {'articles': articles}
    )