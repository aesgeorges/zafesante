from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from articles.models import Infocard, Articles
from datetime import datetime
from django.shortcuts import render, get_object_or_404

# Create your views here.

index_template = 'home/index.html'
register_template = 'registration/register.html'


def index(request):
    cards = Infocard.objects.order_by('created').order_by('-created')
    articles = Articles.objects.filter(published=True).order_by('-created')
    year = datetime.now().year
    for card in cards:
        print(card)
    title = 'Zafè Sante'
    message = 'Se mèt ko ki veye ko.'
    context = {'title': title, 'message': message, 'cards': cards, 'articles': articles}
    return render(request, index_template, context)

def single_article(request, slug):
    article = get_object_or_404(Articles, slug=slug)
    title = article.title
    context = {'article': article, 'title': title}
    return render(request, article_template, context)

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('questions')
    else:
        form = UserCreationForm()
    return render(request, register_template, {'form': form})
