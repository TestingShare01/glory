# Generated by Django 3.1.7 on 2022-01-04 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glory', '0008_task_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='updatetime',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
    ]
