# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ad(models.Model):
    chat_name = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    body = models.CharField(max_length=6000, blank=True, null=True)
    profession = models.CharField(max_length=30, blank=True, null=True)
    time_of_public = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad'


class Ba(models.Model):
    chat_name = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    body = models.CharField(max_length=6000, blank=True, null=True)
    profession = models.CharField(max_length=30, blank=True, null=True)
    time_of_public = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ba'


class Backend(models.Model):
    chat_name = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    body = models.CharField(max_length=6000, blank=True, null=True)
    profession = models.CharField(max_length=30, blank=True, null=True)
    time_of_public = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'backend'


class Designer(models.Model):
    chat_name = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    body = models.CharField(max_length=6000, blank=True, null=True)
    profession = models.CharField(max_length=30, blank=True, null=True)
    time_of_public = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'designer'


class Devops(models.Model):
    chat_name = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    body = models.CharField(max_length=6000, blank=True, null=True)
    profession = models.CharField(max_length=30, blank=True, null=True)
    time_of_public = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devops'


class Frontend(models.Model):
    chat_name = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    body = models.CharField(max_length=6000, blank=True, null=True)
    profession = models.CharField(max_length=30, blank=True, null=True)
    time_of_public = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frontend'


class Fullstack(models.Model):
    chat_name = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    body = models.CharField(max_length=6000, blank=True, null=True)
    profession = models.CharField(max_length=30, blank=True, null=True)
    time_of_public = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fullstack'


class Game(models.Model):
    chat_name = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    body = models.CharField(max_length=6000, blank=True, null=True)
    profession = models.CharField(max_length=30, blank=True, null=True)
    time_of_public = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game'


class Hr(models.Model):
    chat_name = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    body = models.CharField(max_length=6000, blank=True, null=True)
    profession = models.CharField(max_length=30, blank=True, null=True)
    time_of_public = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr'


class Marketing(models.Model):
    chat_name = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    body = models.CharField(max_length=6000, blank=True, null=True)
    profession = models.CharField(max_length=30, blank=True, null=True)
    time_of_public = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marketing'


class Mobile(models.Model):
    chat_name = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    body = models.CharField(max_length=6000, blank=True, null=True)
    profession = models.CharField(max_length=30, blank=True, null=True)
    time_of_public = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mobile'


class NoSort(models.Model):
    chat_name = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    body = models.CharField(max_length=6000, blank=True, null=True)
    profession = models.CharField(max_length=30, blank=True, null=True)
    time_of_public = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'no_sort'


class Pm(models.Model):
    chat_name = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    body = models.CharField(max_length=6000, blank=True, null=True)
    profession = models.CharField(max_length=30, blank=True, null=True)
    time_of_public = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pm'


class Product(models.Model):
    chat_name = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    body = models.CharField(max_length=6000, blank=True, null=True)
    profession = models.CharField(max_length=30, blank=True, null=True)
    time_of_public = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class Qa(models.Model):
    chat_name = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    body = models.CharField(max_length=6000, blank=True, null=True)
    profession = models.CharField(max_length=30, blank=True, null=True)
    time_of_public = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qa'


class Users(models.Model):
    id_user = models.IntegerField(blank=True, null=True)
    api_id = models.IntegerField(blank=True, null=True)
    api_hash = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
