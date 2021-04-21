from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.views import CreateUserViewSet


router = DefaultRouter()
#router.register(r'users', UserViewSet)
router.register(r'users/signup/', CreateUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]