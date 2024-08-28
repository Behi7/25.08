from django.urls import path, include
from . import views

urlpatterns = [
    path('log-in', views.login_user, name='login'),
    path('', views.listquiz, name='listquiz'),
    path('quiz/<int:quiz_id>/', views.listquestion, name='listquestion'),
    path('createquiz', views.createquiz, name='createquiz'),
    path('log_out', views.log_out, name='log_out'),
    path('quiz/<int:quiz_id>/createquestion/', views.createquestion, name='createquestion'),
    path('quiz/<int:quiz_id>/createquestion/<int:id>/option', views.listoption, name='listoption'),
    path('deletequiz/<int:id>/', views.deletequiz, name='deletequiz'),
    path('quiz/<int:quiz_id>/deletequestion/<int:id>/', views.deletequestion, name='deletequestion'),
    path('quiz/<int:quiz_id>/createquestion/<int:id>/option/create', views.createoption, name='createoption'),
    path('register', views.register_user, name='register'),
    path('quiz/<int:quiz_id>/createquestion/<int:question_id>/option/delete/<int:id>', views.deleteOption, name='deleteoption'),
    path('quiz/<int:quiz_id>/createquestion/<int:question_id>/option/update/<int:id>', views.updateoption, name='updateoption')
]