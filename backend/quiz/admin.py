from django.contrib import admin
from quiz.models import Quiz, Question, Category, Answer


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = [
        'name',
        ]

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
	list_display = [
        'id', 
        'title',
        'category',
        'date_created'
        ]

class AnswerInlineModel(admin.TabularInline):
    model = Answer
    extra = 2
    fields = [
        'answer_text', 
        'is_right'
        ]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'quiz',
        'title',
        'technique',
        'score'
        ]
    list_display = [
        'title', 
        'quiz',
        'technique',
        'score',
        'date_updated'
        ]
    inlines = [
        AnswerInlineModel, 
        ] 

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'question',
        'answer_text', 
        'is_right'
        ]