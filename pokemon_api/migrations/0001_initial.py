# Generated by Django 5.1.7 on 2025-04-07 18:36

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('pokemon_id', models.IntegerField()),
                ('types', models.JSONField()),
                ('abilities', models.JSONField()),
                ('base_stats', models.JSONField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('sprite_url', models.URLField()),
            ],
        ),
    ]
