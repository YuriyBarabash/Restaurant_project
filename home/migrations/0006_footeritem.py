# Generated by Django 5.0.3 on 2024-05-04 12:22

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_bestphrases_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', ckeditor.fields.RichTextField()),
                ('phone', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('working_hours', ckeditor.fields.RichTextField()),
                ('twitter', models.URLField(blank=True, max_length=255)),
                ('facebook', models.URLField(blank=True, max_length=255)),
                ('instagram', models.URLField(blank=True, max_length=255)),
                ('youtube', models.URLField(blank=True, max_length=255)),
            ],
        ),
    ]