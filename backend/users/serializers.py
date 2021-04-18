from rest_framework import serializers
from django.contrib.auth.models import User


# class UserUpdateSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = (
#             'email', 
#             'username',
#             'description'
#         )
    

class UserSerializer(serializers.ModelSerializer):
   #user = serializers.StringRelatedField(read_only=True)
   class Meta:
        model = User
        fields = (
            'email', 
            'username', 
            'password'
        )
        
        extra_kwargs = {
            'password': {'write_only': True}
        }
   
    # def create(self, validated_data):
    #     return User.objects.create_user(**validated_data)