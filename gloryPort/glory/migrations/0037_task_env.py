# Generated by Django 3.1.7 on 2022-01-22 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glory', '0036_environment'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='env',
            field=models.CharField(default='', max_length=100, verbose_name='环境'),
        ),
    ]
