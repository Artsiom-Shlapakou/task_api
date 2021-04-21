from rest_framework import serializers
from django.contrib.auth import authenticate


# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()

#     def validate(self, attrs):
#         user = authenticate(username=attrs['username'], password=attrs['password'])
#         print(attrs)
#         if not user:
#             raise serializers.ValidationError('Incorrect email or password')

#         if not user.is_active:
#             return serializers.ValidationError('User is disabled')

#         return {'user': user}
