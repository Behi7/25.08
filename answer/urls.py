from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.answerlist, name='answerlist'),
    path('detail/<int:id>', views.answerdetail, name='detailanswer'),
    path('delete/<int:id>', views.deleteanswer, name = 'deleteanswer'),
    path('get-quiz/<int:id>', views.getQuiz, name='getquiz'),
    path('answerquiz', views.quizlist, name='answerquiz'),
    path('makeanswer/<int:id>', views.makeAnswer, name='makeanswer')
]