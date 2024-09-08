from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('quizzes/', views.QuizListCreateView.as_view(), name='quizcreate'),
    path('quizzes/<int:pk>/', views.QuizDetailView.as_view(), name='quizdetail'),
    path('questions/', views.QuestionListCreateView.as_view(), name='questioncreate'),
    path('questions/<int:pk>/', views.QuestionDetailView.as_view(), name='questionetail'),
    path('options/', views.OptionListCreateView.as_view(), name = 'optioncreate'),
    path('options/<int:id>/', views.OptionDetailView.as_view(), name='optiondetail'),
    path('answers/', views.AnswerListCreateView.as_view(), name='answercreate'),
    path('answers/<int:pk>/', views.AnswerView.as_view(), name='answer'),
    path('answerdetail/', views.AnswerDetailListview.as_view(), name='answerdetaillist'),
    path('answerdetail/<int:id>', views.AnswerDetailview.as_view(), name='answerdetail')
]