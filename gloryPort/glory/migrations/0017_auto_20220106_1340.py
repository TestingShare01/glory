# Generated by Django 3.1.7 on 2022-01-06 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glory', '0016_auto_20220106_1337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caseresult',
            name='msg',
        ),
        migrations.AddField(
            model_name='caseresult',
            name='status',
            field=models.CharField(default=1, max_length=500, verbose_name='状态'),
            preserve_default=False,
        ),
    ]
