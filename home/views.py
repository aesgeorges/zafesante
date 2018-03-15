from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.

index_template = 'home/index.html'
register_template = 'registration/register.html'


def index(request):
    title = 'Zafè Sante'
    message = 'Se mèt ko ki veye ko.'
    context = {'title': title, 'message': message}
    return render(request, index_template, context)


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
