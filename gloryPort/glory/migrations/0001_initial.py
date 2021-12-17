# Generated by Django 3.1.7 on 2021-12-05 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300, verbose_name='项目名称')),
                ('describe', models.CharField(max_length=500, verbose_name='描述')),
                ('jk_num', models.IntegerField(verbose_name='接口数量')),
                ('case_num', models.IntegerField(verbose_name='用例数量')),
                ('updatetime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'db_table': 'project',
            },
        ),
    ]
