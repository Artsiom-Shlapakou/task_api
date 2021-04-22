from django.urls import path, include
from rest_framework.routers import DefaultRouter
from quiz.views import (QuizViewSet, RandomQuestionViewSet,
                        QuizQuestionViewSet, QuizResultViewSet)


router = DefaultRouter()
router.register(r'', QuizViewSet)


urlpatterns = [
    path('quizzes/', include(router.urls), name='quiz'),
    # path('quizzes/r/<str:topic>/', RandomQuestionAPIView.as_view(), name='random' ),
    # path('quizzes/q/<str:topic>/', QuizQuestionAPIView.as_view(), name='questions' ),
    # path('quizzes/<str:topic>/result/', QuizResultAPIView.as_view(), name='quizresults' ),
]