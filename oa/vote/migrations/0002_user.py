# Generated by Django 2.1.8 on 2019-10-11 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('regdate', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
            ],
            options={
                'db_table': 'tb_user',
            },
        ),
    ]
