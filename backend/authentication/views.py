from django.contrib.auth import login, logout
from rest_framework import viewsets, permissions, response, status
from authentication.serializers import LoginSerializer


class LoginView(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = serializers.LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return response.Response(status=status.HTTP_202_ACCEPTED)


class LogoutView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        logout(request.user)
        return response.Response(
            status=status.HTTP_401_UNAUTHORIZED
        )