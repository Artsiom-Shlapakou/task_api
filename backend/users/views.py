from rest_framework import viewsets, request, status
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from users.models import User
from users.serializers import UserSerializer, CreateUserSerializer
from users.permissions import IsOwnerOrReadOnly


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

#     def get_serializer_class(self):
#         if self.action == "create":
#             return CreateUserSerializer
#         return UserSerializer

class CreateUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

    # POST request
    @csrf_exempt
    def create(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        if self.action == "create":
            return CreateUserSerializer
        return UserSerializer