from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.


class NewUser(AbstractUser):
    jwt_secret = models.UUIDField(default=uuid.uuid4())

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        pass

def jwt_get_secret_key(NewUser):
    return NewUser.jwt_secret