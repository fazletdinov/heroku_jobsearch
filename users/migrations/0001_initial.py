# Generated by Django 3.1.14 on 2022-09-16 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_name', models.CharField(blank=True, max_length=150, null=True)),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('body', models.CharField(blank=True, max_length=6000, null=True)),
                ('profession', models.CharField(blank=True, max_length=30, null=True)),
                ('time_of_public', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_name', models.CharField(blank=True, max_length=150, null=True)),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('body', models.CharField(blank=True, max_length=6000, null=True)),
                ('profession', models.CharField(blank=True, max_length=30, null=True)),
                ('time_of_public', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ba',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Backend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_name', models.CharField(blank=True, max_length=150, null=True)),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('body', models.CharField(blank=True, max_length=6000, null=True)),
                ('profession', models.CharField(blank=True, max_length=30, null=True)),
                ('time_of_public', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'backend',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Designer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_name', models.CharField(blank=True, max_length=150, null=True)),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('body', models.CharField(blank=True, max_length=6000, null=True)),
                ('profession', models.CharField(blank=True, max_length=30, null=True)),
                ('time_of_public', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'designer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Devops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_name', models.CharField(blank=True, max_length=150, null=True)),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('body', models.CharField(blank=True, max_length=6000, null=True)),
                ('profession', models.CharField(blank=True, max_length=30, null=True)),
                ('time_of_public', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'devops',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Frontend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_name', models.CharField(blank=True, max_length=150, null=True)),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('body', models.CharField(blank=True, max_length=6000, null=True)),
                ('profession', models.CharField(blank=True, max_length=30, null=True)),
                ('time_of_public', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'frontend',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fullstack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_name', models.CharField(blank=True, max_length=150, null=True)),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('body', models.CharField(blank=True, max_length=6000, null=True)),
                ('profession', models.CharField(blank=True, max_length=30, null=True)),
                ('time_of_public', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'fullstack',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_name', models.CharField(blank=True, max_length=150, null=True)),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('body', models.CharField(blank=True, max_length=6000, null=True)),
                ('profession', models.CharField(blank=True, max_length=30, null=True)),
                ('time_of_public', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'game',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_name', models.CharField(blank=True, max_length=150, null=True)),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('body', models.CharField(blank=True, max_length=6000, null=True)),
                ('profession', models.CharField(blank=True, max_length=30, null=True)),
                ('time_of_public', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'hr',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Marketing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_name', models.CharField(blank=True, max_length=150, null=True)),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('body', models.CharField(blank=True, max_length=6000, null=True)),
                ('profession', models.CharField(blank=True, max_length=30, null=True)),
                ('time_of_public', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'marketing',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_name', models.CharField(blank=True, max_length=150, null=True)),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('body', models.CharField(blank=True, max_length=6000, null=True)),
                ('profession', models.CharField(blank=True, max_length=30, null=True)),
                ('time_of_public', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'mobile',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NoSort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_name', models.CharField(blank=True, max_length=150, null=True)),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('body', models.CharField(blank=True, max_length=6000, null=True)),
                ('profession', models.CharField(blank=True, max_length=30, null=True)),
                ('time_of_public', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'no_sort',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_name', models.CharField(blank=True, max_length=150, null=True)),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('body', models.CharField(blank=True, max_length=6000, null=True)),
                ('profession', models.CharField(blank=True, max_length=30, null=True)),
                ('time_of_public', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pm',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_name', models.CharField(blank=True, max_length=150, null=True)),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('body', models.CharField(blank=True, max_length=6000, null=True)),
                ('profession', models.CharField(blank=True, max_length=30, null=True)),
                ('time_of_public', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Qa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_name', models.CharField(blank=True, max_length=150, null=True)),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('body', models.CharField(blank=True, max_length=6000, null=True)),
                ('profession', models.CharField(blank=True, max_length=30, null=True)),
                ('time_of_public', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'qa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField(blank=True, null=True)),
                ('api_id', models.IntegerField(blank=True, null=True)),
                ('api_hash', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Электронная почта')),
                ('is_active', models.BooleanField(default=True, verbose_name='Статус')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Статус админа')),
                ('is_verify', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('myuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.myuser')),
                ('name', models.CharField(max_length=100)),
                ('family', models.CharField(max_length=100)),
                ('patronymic', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('pol', models.BooleanField(default=False)),
                ('country', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('emails', models.EmailField(max_length=100)),
                ('mobile', models.IntegerField()),
                ('about_me', models.TextField()),
                ('social', models.URLField()),
                ('cv', models.URLField()),
                ('portfolio', models.URLField()),
                ('educational_institution', models.CharField(max_length=150)),
                ('educational_institution_date', models.BooleanField(default=False)),
                ('specialization', models.CharField(max_length=150)),
                ('specialization_text', models.TextField()),
                ('language', models.CharField(max_length=70)),
                ('language_lvl_picmenno', models.CharField(max_length=70)),
                ('language_lvl_yctno', models.CharField(max_length=70)),
                ('hard_skills', models.CharField(max_length=255)),
                ('soft_skills', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('users.myuser',),
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=255)),
                ('looking_for_a_specialist', models.CharField(max_length=255)),
                ('spialization', models.CharField(max_length=150)),
                ('programming_language', models.CharField(max_length=150)),
                ('type_of_activity', models.CharField(max_length=150)),
                ('framework', models.CharField(max_length=150)),
                ('soft_and_services', models.CharField(max_length=255)),
                ('specialist_level', models.CharField(max_length=150)),
                ('payment_amount', models.IntegerField()),
                ('paymant', models.BooleanField(default=False)),
                ('job_description', models.TextField()),
                ('required_work_experience', models.CharField(max_length=20)),
                ('type_of_work', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=150)),
                ('location_bool', models.BooleanField(default=False)),
                ('type_of_employment', models.CharField(max_length=50)),
                ('working_draft', models.CharField(max_length=255)),
                ('duration_of_work', models.CharField(max_length=255)),
                ('hard_skills', models.CharField(max_length=1000)),
                ('soft_skills', models.CharField(max_length=1000)),
                ('language', models.CharField(max_length=50)),
                ('language_picmen', models.CharField(max_length=50)),
                ('language_yctno', models.CharField(max_length=50)),
                ('quation1', models.CharField(max_length=150)),
                ('quation2', models.CharField(max_length=150)),
                ('quation3', models.CharField(max_length=150)),
                ('health', models.BooleanField(default=False)),
                ('food', models.BooleanField(default=False)),
                ('working_conditions', models.BooleanField(default=False)),
                ('education', models.BooleanField(default=False)),
                ('finance_and_guarantees', models.BooleanField(default=False)),
                ('entertainments', models.BooleanField(default=False)),
                ('transport', models.BooleanField(default=False)),
                ('job_manager', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telephon', models.IntegerField()),
                ('responses', models.BooleanField(default=False)),
                ('receive_notifications', models.BooleanField(default=False)),
                ('archive_it', models.BooleanField(default=False)),
                ('when_to_publish', models.BooleanField(default=False)),
                ('automatic_notification', models.BooleanField(default=False)),
                ('additionally', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancyes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hard_skills', models.CharField(max_length=100)),
                ('soft_skills', models.CharField(max_length=100)),
                ('desired_position', models.CharField(max_length=150)),
                ('desired_payment', models.IntegerField()),
                ('photo', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d')),
                ('desired_place_of_work', models.CharField(max_length=1000)),
                ('about_me', models.CharField(max_length=3000)),
                ('checkbox', models.BooleanField(default=False)),
                ('direction_of_activity', models.CharField(max_length=100)),
                ('type_of_company', models.CharField(max_length=100)),
                ('cv', models.CharField(max_length=1000)),
                ('resume', models.FileField(upload_to='resume/%Y/%m/%d')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
