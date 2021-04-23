from rest_framework import serializers
from homework.models import HomeWork, HomeWorkResult
from users.serializers import UserSerializer



class HomeWorkSerializer(serializers.ModelSerializer): 

    class Meta:
        model = HomeWork
        field = [
            'title',
            'description'
        ]

class HomeWorkResultSerializer(serializers.ModelSerializer):
    file_answer = serializers.FileField(max_length=100, use_url=True)   
    user = UserSerializer(read_only=True)
    homework = HomeWorkSerializer(read_only=True)

    class Meta:
        model = HomeWork
        field = [
            'user',
            'homework',
            'file_answer',
            'note',
            'created', 
            'deadline', 
            'mark', 
            'status'
        ]
        read_only_fields = ('created', 'deadline', 'mark', 'status')