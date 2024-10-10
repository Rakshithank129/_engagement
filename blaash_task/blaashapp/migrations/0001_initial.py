# Generated by Django 5.1 on 2024-10-09 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='engagement_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_id', models.PositiveIntegerField()),
                ('post_type', models.CharField(choices=[('video', 'video'), ('story', 'story')], max_length=10)),
                ('post_title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]