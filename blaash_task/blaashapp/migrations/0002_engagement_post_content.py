# Generated by Django 5.1 on 2024-10-09 06:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blaashapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='engagement_post_content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_url', models.URLField(max_length=500)),
                ('story_id', models.CharField(max_length=100)),
                ('engangementpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='blaashapp.engagement_post')),
            ],
        ),
    ]
