from django.shortcuts import render, redirect
from . import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
def listquiz(request):
    quizes = models.Quiz.objects.filter(author=request.user)
    context = {'quizes':quizes}
    return render(request, 'dashboard/listquiz.html', context)


def createquiz(request):
    if request.method == 'POST':
        models.Quiz.objects.create(
            name = request.POST['name'],
            author = request.user
    )
        return redirect('listquiz')
    return render(request, 'dashboard/createquiz.html')

def deletequiz(request, id):
    models.Quiz.objects.get(id=id).delete()
    return redirect('listquiz')

def listquestion(request, quiz_id):
    quiz = models.Quiz.objects.get(id=quiz_id)
    questions = models.Question.objects.filter(quiz=quiz)
    context = {'questions':questions, 'quiz':quiz}
    return render(request, 'dashboard/listquestion.html', context)

def listoption(request, quiz_id, id):
    context = {}
    quiz_id = models.Quiz.objects.get(id=quiz_id)
    question = models.Question.objects.get(id=id)
    context['options'] = models.Option.objects.filter(question = question)
    context['quiz'] = quiz_id
    context['question'] = question
    return render(request, 'dashboard/listoption.html', context)

def createquestion(request, quiz_id):
    context = {}
    quiz = models.Quiz.objects.get(id=quiz_id)
    if request.method == "POST":
        question =  models.Question.objects.create(
            name = request.POST['name'],
            quiz = quiz
        )
        context['question'] = question
        return redirect('listquestion', quiz.id)
    context['quiz'] = quiz
    return render(request, 'dashboard/createquestion.html', context)

def deletequestion(request, quiz_id, id):
    quiz = models.Quiz.objects.get(id=quiz_id)
    context = {'quiz':quiz}
    models.Question.objects.get(id=id).delete()
    return redirect('listquestion', quiz_id=quiz_id)

def createoption(request, quiz_id, id):
    context = {}
    quiz = models.Quiz.objects.get(id=quiz_id)    
    question = models.Question.objects.get(id=id)
    context['correct'] = bool(models.Option.objects.filter(question = question))
    if request.method == 'POST':
        if not models.Option.objects.filter(question = question):
            models.Option.objects.create(
                name = request.POST['name'],
                question = question,
                correct = True
            )
            return redirect('listoption', quiz_id, question.id)
        else:
            models.Option.objects.create(
                name = request.POST['name'],
                question = question,
                correct = False
            )
            return redirect('listoption', quiz_id, question.id)

    context['quiz'] = quiz
    context['question'] = question
    return render(request, 'dashboard/createoption.html', context)

def log_out(request):
    logout(request)
    return redirect('listquiz')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('listquiz')
        else:
            return redirect('login')
    return render(request, 'dashboard/login.html')

def register_user(request):
    context={}
    try:
        if request.method == 'POST':
            User.objects.create_user(
                username = request.POST['username'],
                password = request.POST['password'],
            )
            return redirect('login')
    except:
        context={'error':'bunday login bor'}
    return render(request, 'dashboard/register.html', context)

def deleteOption(request, quiz_id, question_id, id):
    models.Option.objects.get(id=id).delete()
    return redirect('listoption', quiz_id, question_id)

def updateoption(request, quiz_id, question_id, id):
    update = models.Option.objects.get(id=id)
    if request.method == 'POST':
        update.name = request.POST['name']
        update.save()
        return redirect('listoption', quiz_id, question_id)
    return render(request, 'dashboard/createoption.html', {'update':update, 'quiz_id':quiz_id, 'question_id':question_id})