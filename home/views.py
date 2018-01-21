from django.shortcuts import render

# Create your views here.

index_template = 'home/index.html'


def index(request):
    title = 'Byenvini sou Zafè Sante'
    message = 'Se mèt ko ki veye ko.'
    context = {'title': title, 'message': message}
    return render(request, index_template, context)
