from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    '''
    Custom user class.
    '''
    username = models.CharField('username', max_length=20, unique=True, db_index=True)
    password = models.CharField('password', max_length=200)
    first_name = models.CharField('first name', max_length=200, blank=True)
    last_name = models.CharField('last name', max_length=200, blank=True)
    email = models.EmailField('email address', unique=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
