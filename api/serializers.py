from rest_framework import serializers
from main import models


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Option
        fields = ['id', 'name', 'correct']

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = models.Question
        fields = ['id', 'name', 'quiz', 'options']
 
class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = models.Quiz
        fields = ['id', 'name', 'author', 'questions']

class AnswerDetailSerializer(serializers.ModelSerializer):
    is_correct = serializers.BooleanField(read_only=True)

    class Meta:
        model = models.AnswerDetail
        fields = ['id', 'answer', 'question', 'user_choice', 'is_correct']

class AnswerSerializer(serializers.ModelSerializer):
    answer_details = AnswerDetailSerializer(many=True, read_only=True)

    class Meta:
        model = models.Answer
        fields = ['id', 'quiz', 'author', 'answer_details']
