from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from .models import Questions

# Create your views here.
question_template = 'questions/question.html'
questions_list_template = 'questions/list.html'


def questions_list(request):
    questions = Questions.objects.all().order_by('created')
    title = 'Kesyon'
    year = datetime.now().year
    context = {'questions': questions, 'title': title, 'year': year}
    return render(request, questions_list_template, context)


def single_question(request, slug):
    question = get_object_or_404(Questions, slug=slug)
    context = {'question': question}
    return render(request, question_template, context)


def vote(request, slug):
    question = get_object_or_404(Questions, slug=slug)
    question.votes += 1
    question.save()
    return redirect('questions')
