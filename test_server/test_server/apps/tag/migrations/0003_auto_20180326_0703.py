# Generated by Django 2.0.1 on 2018-03-26 07:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import test_server.apps.uidgenerator.models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0002_tag_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tags', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_id',
            field=test_server.apps.uidgenerator.models.UIDField(blank=True, primary_key=True, serialize=False),
        ),
    ]