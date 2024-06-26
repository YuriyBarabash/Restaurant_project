# Generated by Django 5.0.3 on 2024-05-04 14:42

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Address',
            },
        ),
        migrations.CreateModel(
            name='FollowUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=100)),
                ('text', ckeditor.fields.RichTextField()),
                ('email', ckeditor.fields.RichTextField()),
                ('phone', ckeditor.fields.RichTextField()),
                ('social_media', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name_plural': 'Follow Us',
            },
        ),
    ]
