# Generated by Django 3.1.7 on 2021-07-15 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_auto_20210715_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='companyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(default='', max_length=255)),
                ('address', models.CharField(default='', max_length=255)),
                ('contact', models.CharField(default='', max_length=13)),
                ('companyemail', models.EmailField(max_length=254)),
                ('username', models.CharField(default='', max_length=255)),
                ('password', models.CharField(default='', max_length=255)),
                ('user', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
