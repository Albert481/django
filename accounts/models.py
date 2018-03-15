from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Please set an email')
        if not password:
            raise ValueError('Please set a password')

        email = self.normalize_email(email)
        user_obj = self.model(email=email, is_staff=is_staff, is_active=True, is_superuser=is_superuser, **extra_fields)
        user_obj.set_password(password)
        user_obj.save(using=self.db)
        return user_obj

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)

class Auth_User(AbstractBaseUser):
    email = models.EmailField(unique=True, primary_key=True)
    staff = models.BooleanField(default=False) #staff user, but not superuser
    admin = models.BooleanField(default=False) #superuser

    USERNAME_FIELD = 'email'

    objects = UserManager()


class Profile(models.Model):
    email = models.CharField(max_length=255, default='null', primary_key=True)
    ethaddress = models.CharField(max_length=255, default='null')
    indicativecontribution = models.DecimalField(max_digits=5, default=0, decimal_places=2)
    actualcontribution = models.DecimalField(max_digits=5, default=0, decimal_places=2)
    mytoken = models.DecimalField(max_digits=5, default=0, decimal_places=2)
    bonustoken = models.DecimalField(max_digits=5, default=0, decimal_places=2)
    tokenwithdrawn = models.DecimalField(max_digits=5, default=0, decimal_places=2)