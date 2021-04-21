from django.urls import include, path
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users/', CreateUserViewSet)

user_patterns = [
    path('', include(router.urls)),
    path('signup/', include(router.urls)),
]