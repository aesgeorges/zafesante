from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import Articles

# Create your views here.
article_template = 'articles/article.html'
article_blog_template = 'articles/blog.html'


def articles_blog(request):
    articles = Articles.objects.filter(published=True).order_by('-created')
    title = 'Atik Zafè Sante'
    year = datetime.now().year
    context = {'articles': articles, 'title': title, 'year': year}
    return render(request, article_blog_template, context)


def single_article(request, slug):
    article = get_object_or_404(Articles, slug=slug)
    title = article.title
    text = article.content
    description = article.description
    context = {'article': article, 'title': title, 'text': text, 'description': description}
    return render(request, article_template, context)
