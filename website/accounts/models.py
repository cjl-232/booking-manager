from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

class UserManager(BaseUserManager):

    def _create_user(
        self,
        email,
        password,
        is_staff,
        is_superuser,
    ):
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email = email,
            is_active = True,
            is_staff = is_staff,
            is_superuser = is_superuser,
            date_joined = now,
            last_login = now,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_user(self, email, password):
        return self._create_user(email, password, False, False)
        
    def create_superuser(self, email, password):
        return self._create_user(email, password, True, True)

class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique = True)
    name = models.CharField(max_length = 254, null = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    date_joined = models.DateTimeField(auto_now_add = True)
    last_login = models.DateTimeField(null = True)
    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'accounts_users'