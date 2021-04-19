from rest_framework import serializers
from users.models import User
    

class UserSerializer(serializers.ModelSerializer):
  
   class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email', 
            'username', 
            'password'
        )

class CreateUserSerializer(serializers.ModelSerializer):
    
    def save(self, *args, **kwargs):
        user = User(
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        user.set_password(self.validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email', 
            'username', 
            'password'
        )
   
    # def create(self, validated_data):
    #     return User.objects.create_user(**validated_data)
