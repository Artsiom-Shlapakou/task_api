from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import settings
from users.models import User

# for automatically generated Token. 
# link: https://www.django-rest-framework.org/api-guide/authentication/
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)