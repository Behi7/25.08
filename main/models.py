from django.db import models
from django.contrib.auth.models import User


# Question
class Quiz(models.Model):
    name = models.CharField(max_length=100) 
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    @property
    def questions(self):
        return Question.objects.filter(quiz=self)


class Question(models.Model):
    name = models.CharField(max_length=255)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    @property
    def options(self):
        return Option.objects.filter(question=self)

    @property
    def correct_option(self):
        return Option.objects.get(question=self, correct=True)
    

class Option(models.Model):
    name = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

# Answer
class Answer(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author.username} -> {self.quiz.name}"


class AnswerDetail(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_choice = models.ForeignKey(Option, on_delete=models.CASCADE)

    @property
    def is_correct(self):
        return self.user_choice == self.question.correct_option
