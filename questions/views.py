from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from datetime import datetime
from .models import Questions, Voted
from django.contrib.auth.decorators import login_required

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


@login_required(login_url='login')
def vote(request, slug):
    question = get_object_or_404(Questions, slug=slug)
    vote, created = Voted.objects.get_or_create(user=request.user, question=question)
    if not created:
        questions = Questions.objects.all().order_by('created')
        title = 'Kesyon'
        error = 'Sorry, you cannot vote more than once.'
        context = {'questions': questions, 'title': title, 'error': error}
        return render(request, questions_list_template, context)
    else:
        question.votes += 1
        question.save()
        return redirect('questions')
