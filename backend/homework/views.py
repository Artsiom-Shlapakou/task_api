from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from homework.models import HomeWork, HomeWorkResult
from homework.serializers import HomeWorkSerializer, HomeWorkResultSerializer

class HomeworkViewSet(ModelViewSet):
    
    queryset = HomeWork.objects.all()
    serializer_class = HomeWorkSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user,
                       file_answer=self.request.data.get('file_answer'))

class HomeworkResultViewSet(ModelViewSet):
    
    queryset = HomeWorkResult.objects.all()
    serializer_class = HomeWorkResultSerializer
