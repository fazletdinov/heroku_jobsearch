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
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='resumes')
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

class Vacancy(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vacancyes')
    company = models.CharField(max_length=255)
    whom = models.CharField(max_length=255)
    programming_language = models.CharField(max_length=255)
    framework = models.CharField(max_length=255)
    specialist_level = models.CharField(max_length=255)
    # детали
    payment_amount = models.IntegerField()
    paymant = models.BooleanField(default=False)
    job_description = models.TextField()
    type_of_work = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    type_of_employment = models.CharField(max_length=30)
    working_draft = models.CharField(max_length=255)
    duration_of_work = models.CharField(max_length=255)
    hard_skills = models.CharField(max_length=1000)
    soft_skills = models.CharField(max_length=1000)
    language = models.CharField(max_length=255)
    quation1 = models.CharField(max_length=150)
    quation2 = models.CharField(max_length=150)
    quation3 = models.CharField(max_length=150)
    # бонусы
    health = models.BooleanField(default=False)
    food = models.BooleanField(default=False)
    working_conditions = models.BooleanField(default=False)
    education = models.BooleanField(default=False)
    finance_and_guarantees = models.BooleanField(default=False)
    entertainments = models.BooleanField(default=False)
    transport = models.BooleanField(default=False)
    # контакты
    job_manager = models.CharField(max_length=255)
    email = models.EmailField()
    telephon = models.IntegerField()
    responses = models.CharField(max_length=150)
    receive_notifications = models.BooleanField(default=False)
    archive_it = models.BooleanField(default=False)
    when_to_publish = models.BooleanField(default=False)
    automatic_notification = models.BooleanField(default=False)
    additionally = models.BooleanField(default=False)

