from main import models
from rest_framework import generics
from . import serializers


class QuizListCreateView(generics.ListCreateAPIView):
    queryset = models.Quiz.objects.all()
    serializer_class = serializers.QuizSerializer


class QuizDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Quiz.objects.all()
    serializer_class = serializers.QuizSerializer


class QuestionListCreateView(generics.ListCreateAPIView):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer


class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer


class OptionListCreateView(generics.ListCreateAPIView):
    queryset = models.Option.objects.all()
    serializer_class = serializers.OptionSerializer


class OptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Option.objects.all()
    serializer_class = serializers.OptionSerializer


class AnswerListCreateView(generics.ListCreateAPIView):
    queryset = models.Answer.objects.all()
    serializer_class = serializers.AnswerSerializer


class AnswerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Answer.objects.all()
    serializer_class = serializers.AnswerSerializer

class AnswerDetailview(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.AnswerDetail.objects.all()
    serializer_class = serializers.AnswerDetailSerializer


class AnswerDetailListview(generics.ListCreateAPIView):
    queryset = models.AnswerDetail.objects.all()
    serializer_class = serializers.AnswerDetailSerializer
