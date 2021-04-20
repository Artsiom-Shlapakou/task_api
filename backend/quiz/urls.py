from django.urls import path, include
from rest_framework.routers import DefaultRouter
from quiz.views import QuizViewSet, RandomQuestionAPIView, QuizQuestionAPIView


router = DefaultRouter()
router.register('quizzes/', QuizViewSet)


urlpatterns = [
    path('', include(router.urls), name='quiz'),
    # path('r/<str:topic>/', RandomQuestionAPIView.as_view(), name='random' ),
    # path('q/<str:topic>/', QuizQuestionAPIView.as_view(), name='questions' ),
]