# Generated by Django 3.0.8 on 2020-07-20 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ph', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(max_length=10)),
                ('aadhar', models.ImageField(upload_to='images/aadhar')),
                ('aadharno', models.CharField(max_length=20, null=True)),
                ('pancard', models.ImageField(upload_to='images/pancard')),
                ('pancardno', models.CharField(max_length=20, null=True)),
                ('bankst', models.ImageField(upload_to='images/bankst')),
                ('photo', models.ImageField(upload_to='images/photo')),
                ('li', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
