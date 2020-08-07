from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, first_name, last_name):
        if not email:
            raise ValueError('Users must have an email address')
        if not first_name:
            raise ValueError('Users must have first name')
        if not last_name:
            raise ValueError('Users must have a last name')
        now = timezone.now()
        email = self.normalize_email(email)

        user = self.model(
            email=email,
            is_staff=is_staff, 
            is_active=True,
            is_superuser=is_superuser, 
            last_login=now,
            date_joined=now, 
            first_name=first_name,
            last_name =last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, first_name, last_name):
        return self._create_user(email, password, False, False, first_name, last_name) 

    def create_superuser(self, email, password, first_name, last_name):
        user=self._create_user(email, password, True, True, first_name, last_name)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=60, unique=True, blank=True, null=True) 
    first_name = models.CharField(max_length=254, null=True, blank=True)
    last_name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    


    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.first_name

    def get_username(self):
        return self.username
    
    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)

    def has_perms(self, perm_list, obj=None):
        return super().has_perms(perm_list, obj=obj)
    
    def has_module_perms(self, app_label):
        return super().has_module_perms(app_label)

