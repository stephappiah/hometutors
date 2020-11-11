from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, fullname):
        if not email:
            raise ValueError('Users must have an email address')
        if not fullname:
            raise ValueError('Users must provide fullname')

        now = timezone.now()
        email = self.normalize_email(email)

        user = self.model(
            email=email,
            is_staff=is_staff, 
            is_active=True,
            is_tutor=False,
            is_superuser=is_superuser, 
            last_login=now,
            date_joined=now, 
            fullname=fullname
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, fullname):
        return self._create_user(email, password, False, False, fullname) 

    def create_superuser(self, email, password, fullname):
        user=self._create_user(email, password, True, True, fullname)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=60, unique=True, blank=True, null=True) 
    fullname = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    is_tutor = models.BooleanField(default=False)

    


    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname']

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.fullname

    def get_short_name(self):
        name = self.fullname
        firstname = name.split()[0]
        return firstname 

    def get_username(self):
        return self.username
    
    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)

    def has_perms(self, perm_list, obj=None):
        return super().has_perms(perm_list, obj=obj)
    
    def has_module_perms(self, app_label):
        return super().has_module_perms(app_label)

