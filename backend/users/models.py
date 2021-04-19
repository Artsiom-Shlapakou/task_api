from django.db import models
from django.contrib.auth import get_user_model


# get_user_model() - this method will return the currently active user mode
User = get_user_model()