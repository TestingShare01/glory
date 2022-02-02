# Generated by Django 3.1.7 on 2021-12-31 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glory', '0005_auto_20211230_0844'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='标签名称')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'db_table': 'tag',
            },
        ),
    ]
