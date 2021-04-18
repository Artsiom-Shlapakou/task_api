from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User
from users.serializers import UserSerializer
from users.permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# class Search(ListView):
#     model = User
#     template_name = 'user/table.html'
#     paginate_by = 5

#     def get_queryset(self):
#         find = self.kwargs['find']
#         return self.model.objects.filter(Q(first_name__icontains=find) |
#                                          Q(last_name__icontains=find) |
#                                          Q(second_last_name__icontains=find) |
#                                          Q(role__nombre__icontains=find))