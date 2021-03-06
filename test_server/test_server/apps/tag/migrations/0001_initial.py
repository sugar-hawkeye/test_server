# Generated by Django 2.0.1 on 2018-03-15 01:41

from django.db import migrations, models
import test_server.apps.uidgenerator.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
                ('tag_id', test_server.apps.uidgenerator.models.UIDField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=15, unique=True, verbose_name='标签名')),
                ('priority', models.IntegerField(blank=True, null=True, verbose_name='排列顺序')),
                ('is_publish', models.BooleanField(default=False, verbose_name='是否发布')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
                'db_table': 'tag',
                'ordering': ['created_at'],
                'get_latest_by': 'created_at',
            },
        ),
    ]
