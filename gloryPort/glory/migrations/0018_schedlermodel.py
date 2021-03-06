# Generated by Django 3.1.7 on 2022-01-07 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glory', '0017_auto_20220106_1340'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchedlerModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('taskid', models.CharField(max_length=200, verbose_name='定时任务id')),
                ('type', models.CharField(max_length=200, verbose_name='定时类型')),
                ('tasktime', models.CharField(max_length=300, verbose_name='任务时间')),
                ('args', models.CharField(max_length=300, verbose_name='参数')),
            ],
            options={
                'db_table': 'SchedlerModel',
            },
        ),
    ]
