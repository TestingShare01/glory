# Generated by Django 3.1.7 on 2022-01-18 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glory', '0031_auto_20220118_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='task_num',
            field=models.CharField(default='', max_length=200, verbose_name='任务名'),
        ),
    ]
