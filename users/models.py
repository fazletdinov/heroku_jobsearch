from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.conf import settings

class MyUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Вы не ввели email')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using='default')
        return user

    def create_user(self, email, password):
        return self._create_user(email, password)

    def create_superuser(self, email, password):
        return self._create_user(email, password, is_staff=True, is_superuser=True)

class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Электронная почта', max_length=100, unique=True)
    is_active = models.BooleanField('Статус', default=True)
    is_staff = models.BooleanField('Статус админа', default=False)
    is_verify = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    def __str__(self):
        return self.email

class Resume(models.Model):

    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='resumes')
    hard_skills = models.CharField(max_length=1000)
    soft_skills = models.CharField(max_length=1000)
    desired_position = models.CharField(max_length=150)
    desired_payment = models.IntegerField()
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True)
    desired_place_of_work = models.CharField(max_length=1000)
    about_me = models.CharField(max_length=3000)
    checkbox = models.CharField(max_length=255)
    direction_of_activity = models.CharField(max_length=1000)
    type_of_company = models.CharField(max_length=1000)
    csv = models.CharField(max_length=1000)
    resume = models.FileField(upload_to='resume/%Y/%m/%d')
