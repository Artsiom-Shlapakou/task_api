from django.urls import path, include
from rest_framework.routers import DefaultRouter
from quiz.views import (QuizViewSet, RandomQuestionViewSet,
                        QuizQuestionViewSet, QuizResultViewSet)


router = DefaultRouter()
router.register(r'', QuizViewSet)
router.register(r'r/<str:topic>/', RandomQuestionViewSet, basename='random')
router.register(r'q/<str:topic>/', QuizQuestionViewSet, basename='questions')
router.register(r'<str:topic>/results/', QuizResultViewSet, basename='quizresults')

urlpatterns = [
    path('quizzes/', include(router.urls), name='quiz'),
]