from rest_framework import generics, viewsets
from rest_framework.response import Response
from quiz.models import Quiz, Question
from quiz.serializers import (QuizSerializer, RandomQuestionSerializer, 
                            QuestionSerializer, QuizResultSerializer)
from rest_framework.views import APIView

class QuizViewSet(viewsets.ModelViewSet):

    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class RandomQuestionAPIView(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)

class QuizQuestionAPIView(APIView):

    def get(self, request, format=None, **kwargs):
        quiz = Question.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuestionSerializer(quiz, many=True)
        return Response(serializer.data)

class QuizResultAPIView(APIView):
    
    def get(self, request, format=None, **kwargs):
        queryset = QuizResult.objects.filter(quiz__title=kwargs['topic'])
        serializer_class = AnswerSerializer
        return Response(serializer.data)