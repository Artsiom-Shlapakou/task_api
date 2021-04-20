from rest_framework import serializers
from quiz.models import Quiz, Question, Answer, Category

class CategorySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Category
        fields = [
            'name',
        ]

class QuizSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Quiz
        fields = [
            'category',
            'title',
        ]

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = [
            'id',
            'answer_text',
            'is_right',
        ]

class RandomQuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = [
            'title',
            'answer',
        ]

class QuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)
    quiz = QuizSerializer(read_only=True)

    class Meta:
        model = Question
        fields = [
            'quiz',
            'score',
            'title',
            'answer',
        ]