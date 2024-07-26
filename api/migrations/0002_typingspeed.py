# Generated by Django 5.0.7 on 2024-07-26 09:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TypingSpeed',
            fields=[
                ('id', models.CharField(editable=False, max_length=64, primary_key=True, serialize=False, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('speed', models.IntegerField()),
                ('accuracy', models.FloatField()),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.challenge')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
