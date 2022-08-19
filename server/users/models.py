from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from rest_framework_simplejwt.tokens import RefreshToken


class CustomAccountManager(BaseUserManager):

    def create_user(self, nickname, username, password=None, password2=None, **other_fields):
        if not nickname:
            raise TypeError('Users should have a nickname.')
        if not username:
            raise TypeError('Users should hae a username.')
        
        
        user = self.model(nickname=nickname, username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, nickname, username, password=None, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')

        return self.create_user(nickname, username, password, **other_fields)





class CustomUser(AbstractBaseUser, PermissionsMixin):

    
    username = models.CharField(max_length=45, unique=True)
    nickname = models.CharField(max_length=100, unique=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    
    objects = CustomAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.username
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh':str(refresh),
            'access': str(refresh.access_token)
        }


