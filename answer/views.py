from django.shortcuts import render, redirect
from main import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def answerlist(request):
    answers = models.Answer.objects.filter(author=request.user)
    for answer in answers:
        answerdetail = models.AnswerDetail.objects.filter(answer=answer)
        answer.options = len(answerdetail)
        filtered_correct = 0
        for obj in answerdetail:
            if obj.is_correct == True:
                filtered_correct+=1
        answer.un_correct = answer.options - filtered_correct
        answer.correct = filtered_correct
        if filtered_correct:
            answer.charget = (filtered_correct * 100) / answer.options
        else:
            answer.charget = 0
    return render(request, 'answer/answerquestion.html', {'answers':answers})

def answerdetail(request, id):
    answer = models.Answer.objects.get(id=id)
    detail = models.AnswerDetail.objects.filter(answer = answer)
    return render(request, 'answer/answerdetail.html', {'answerdetails':detail})

def deleteanswer(request, id):
    models.Answer.objects.get(id=id).delete()
    return redirect('answerlist')

def getQuiz(request, id):
    quiz = models.Quiz.objects.get(id=id)
    return render(request, 'answer/answerquiz.html', {'quiz':quiz})

def makeAnswer(request, id):
    quiz = models.Quiz.objects.get(id=id)
    answer = models.Answer.objects.create(quiz=quiz, author=request.user)
    for key, value in request.POST.items():
        if key.isdigit():
            print(models.Option.objects.get(id=int(value)))
            answerdetails = models.AnswerDetail.objects.create(
                answer = answer, 
                question = models.Question.objects.get(id=int(key)), 
                user_choice = models.Option.objects.get(id=int(value)))
    return redirect('answerlist')


def quizlist(request):
    return render(request, 'answer/quizlist.html', {'quizes': models.Quiz.objects.all()})