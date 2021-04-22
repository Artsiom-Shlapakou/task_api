from django.urls import include, path
from rest_framework.routers import DefaultRouter
from homework.views import HomeworkViewSet


router = DefaultRouter()
router.register(r'homework', HomeworkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]