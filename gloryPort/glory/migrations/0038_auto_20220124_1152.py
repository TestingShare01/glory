# Generated by Django 3.1.7 on 2022-01-24 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glory', '0037_task_env'),
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='名称')),
                ('type', models.CharField(max_length=100, verbose_name='通知类型')),
                ('mesId', models.CharField(max_length=100, verbose_name='通知内容ID')),
                ('userId', models.CharField(max_length=100, verbose_name='用户ID')),
                ('ifRead', models.CharField(max_length=100, verbose_name='是否已读')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updatetime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'db_table': 'message',
            },
        ),
        migrations.AlterField(
            model_name='task',
            name='env',
            field=models.CharField(default='', max_length=100, verbose_name='环境id'),
        ),
    ]
