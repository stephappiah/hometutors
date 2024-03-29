from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):

    def _create_user(self, email, contact, password, is_staff, is_superuser, first_name, last_name, is_tutor, is_student, is_guardian):
        if not email:
            raise ValueError('Users must have an email address')
        if not first_name:
            raise ValueError('Users must provide Firstname')
        if not last_name:
            raise ValueError('Users must provide Lastname')

        now = timezone.now()
        email = self.normalize_email(email)

        user = self.model(
            email=email,
            contact=contact,
            is_staff=is_staff, 
            is_active=True,
            is_superuser=is_superuser, 
            last_login=now,
            date_joined=now, 
            first_name=first_name,
            last_name=last_name,
            is_tutor=is_tutor, 
            is_student=is_student, 
            is_guardian=is_guardian
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, contact, password, first_name, last_name):
        return self._create_user(email, contact, password, False, False, first_name, last_name, False, False, False) 

    def create_superuser(self, email, contact, password, first_name, last_name):
        user=self._create_user(email, contact, password, True, True, first_name, last_name, False, False, False)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=60, unique=True, blank=True, null=True) 
    first_name = models.CharField(max_length=254, null=True, blank=True)
    last_name = models.CharField(max_length=254, null=True, blank=True)
    contact = PhoneNumberField(null=True, blank=True, region='GH')
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    is_tutor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_guardian = models.BooleanField(default=False)

    


    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'contact']

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        if self.first_name != None and self.last_name != None:
            return self.first_name + ' ' + self.last_name
        elif self.first_name == None:
            return self.last_name
        else:
            return self.first_name 

    def get_call_contact(self):
        return self.contact

    def get_short_name(self):
        if self.first_name == None:
            return self.last_name
        else:
            return self.first_name

    def get_username(self):
        return self.username
    
    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)

    def has_perms(self, perm_list, obj=None):
        return super().has_perms(perm_list, obj=obj)
    
    def has_module_perms(self, app_label):
        return super().has_module_perms(app_label)

