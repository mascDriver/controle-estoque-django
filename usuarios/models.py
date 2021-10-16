from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.hashers import make_password


class MyUserManager(BaseUserManager):
    def create_user(self, email_usuario, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email_usuario:
            raise ValueError('Users must have an email address')

        user = self.model(
            email_usuario=self.normalize_email(email_usuario),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email_usuario, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email_usuario,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser, PermissionsMixin):
    cod_usuario = models.AutoField(primary_key=True)
    nome_usuario = models.CharField(max_length=50)
    email_usuario = models.CharField(max_length=100, unique=True)
    senha_usuario = models.CharField(max_length=500)
    is_superuser = models.BooleanField(blank=False, null=True)
    is_staff = models.BooleanField(default=True)
    objects = MyUserManager()

    USERNAME_FIELD = 'email_usuario'

    class Meta:
        managed = False
        db_table = 'usuario'

    def get_absolute_url(self):
        return reverse('usuario-list')
        # return reverse('product-update', kwargs={'pk': self.pk})

