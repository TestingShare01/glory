# Generated by Django 3.1.7 on 2022-01-04 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glory', '0007_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.CharField(default=2323, max_length=200, verbose_name='执行者'),
            preserve_default=False,
        ),
    ]
