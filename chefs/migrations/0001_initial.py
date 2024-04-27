# Generated by Django 5.0.3 on 2024-04-27 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chefs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('cuisine', models.CharField(blank=True, max_length=255)),
                ('position', models.PositiveSmallIntegerField()),
                ('photo', models.ImageField(blank=True, upload_to='chefs/')),
                ('is_visible', models.BooleanField(default=True)),
                ('facebook', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('instagram', models.URLField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Chefs',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='HeadExpression',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expression', models.TextField()),
                ('name', models.CharField(max_length=255, unique=True)),
                ('job_title', models.CharField(blank=True, max_length=255)),
                ('position', models.PositiveSmallIntegerField()),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Head Expressions',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='UnderChefsExpression',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expression', models.TextField()),
                ('name', models.CharField(max_length=255, unique=True)),
                ('job_title', models.CharField(blank=True, max_length=255)),
                ('position', models.PositiveSmallIntegerField()),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Under Chefs Expressions',
                'ordering': ('position',),
            },
        ),
    ]
