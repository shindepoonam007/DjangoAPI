# Generated by Django 4.0.1 on 2022-01-31 08:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=100)),
                ('userId', models.IntegerField()),
                ('modifyDate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
