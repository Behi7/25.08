from django.shortcuts import render, redirect
from main import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

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
    for item in detail:
            item.correct = item.question.correct_option
    return render(request, 'answer/answerdetail.html', {'answerdetails':detail, 'id':answer.id})

def deleteanswer(request, id):
    models.Answer.objects.get(id=id).delete()
    return redirect('answerlist')

def getQuiz(request, id):
    quiz = models.Quiz.objects.get(id=id)
    return render(request, 'answer/answerquiz.html', {'quiz':quiz})

# def makeAnswer(request, id):
#     quiz = models.Quiz.objects.get(id=id)
#     answer = models.Answer.objects.create(quiz=quiz, author=request.user)
#     pdf_file = canvas.Canvas("reportlab_example.pdf")
#     pdf_file.setFont("Helvetica", 12)
#     for key, value in request.POST.items():
#         if key.isdigit():
#             print(models.Option.objects.get(id=int(value)))
#             object = models.AnswerDetail.objects.create(
#                 answer = answer, 
#                 question = models.Question.objects.get(id=int(key)), 
#                 user_choice = models.Option.objects.get(id=int(value)))
#             pdf_file.drawString(100, 700, object.question.name)
#             pdf_file.drawString(100, 700, object.user_choice.name)
#     pdf_file.save()        
#     return redirect('answerlist')


def makeAnswer(request, id):
    quiz = models.Quiz.objects.get(id=id)
    answer = models.Answer.objects.create(quiz=quiz, author=request.user)
    data = []
    for key, value in request.POST.items():
        if key.isdigit():
            object = models.AnswerDetail.objects.create(
                answer = answer,
                question = models.Question.objects.get(id=int(key)),
                user_choice = models.Option.objects.get(id=int(value)))
            data.append([object.question.name, object.user_choice.name])
    doc = SimpleDocTemplate(
        f"{request.user}_{quiz.name}.pdf",
        pagesize=A4,
    )
    table = Table(
        data,
        colWidths=[250, 250],
        rowHeights=30,
    )
    style = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
    ])
    table.setStyle(style)
    elements = []
    elements.append(table)
    doc.build(elements)

    return redirect('answerlist')


def quizlist(request):
    return render(request, 'answer/quizlist.html', {'quizes': models.Quiz.objects.all()})