from rest_framework import generics, viewsets
from rest_framework.response import Response
from quiz.models import Quiz, Question
from quiz.serializers import (QuizSerializer, RandomQuestionSerializer, 
                            QuestionSerializer, QuizResultSerializer)


class QuizViewSet(viewsets.ModelViewSet):

    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class RandomQuestionViewSet(viewsets.ModelViewSet):

    def list(self, request, *args, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)

class QuizQuestionViewSet(viewsets.ModelViewSet):

    def list(self, request, *args, **kwargs):
        quiz = Question.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuestionSerializer(quiz, many=True)
        return Response(serializer.data)

class QuizResultViewSet(viewsets.ModelViewSet):
    
    def list(self, request, *args, **kwargs):
        queryset = QuizResult.objects.filter(quiz__title=kwargs['topic'])
        serializer_class = QuizResultSerializer
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        pass
    # def create(self, request, *args, **kwargs):
    #     serializer = QuizResultSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'status': 'Quiz result created successfully'}, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 