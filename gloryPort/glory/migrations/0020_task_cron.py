# Generated by Django 3.1.7 on 2022-01-08 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glory', '0019_schedlermodel_funcname'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='cron',
            field=models.CharField(default=1, max_length=200, verbose_name='定时任务时间'),
            preserve_default=False,
        ),
    ]
