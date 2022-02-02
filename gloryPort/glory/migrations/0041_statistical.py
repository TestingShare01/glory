# Generated by Django 3.1.7 on 2022-01-30 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glory', '0040_caseapi_extractor'),
    ]

    operations = [
        migrations.CreateModel(
            name='statistical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200, verbose_name='统计类型')),
                ('num', models.IntegerField(verbose_name='统计数量')),
            ],
            options={
                'db_table': 'statistical',
            },
        ),
    ]
