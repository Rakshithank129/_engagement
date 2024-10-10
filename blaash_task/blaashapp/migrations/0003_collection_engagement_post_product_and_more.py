# Generated by Django 5.1 on 2024-10-09 09:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blaashapp', '0002_engagement_post_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='engagement_post_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('sku', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='engagement_post_collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blaashapp.collection')),
                ('engagementpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collections', to='blaashapp.engagement_post')),
            ],
        ),
        migrations.CreateModel(
            name='engagement_post_product_mapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=255)),
                ('engagementpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_mapping', to='blaashapp.engagement_post')),
            ],
        ),
    ]
