# Generated by Django 5.0.3 on 2024-04-24 12:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuDish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slag', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField()),
                ('position', models.PositiveSmallIntegerField()),
                ('photo', models.ImageField(blank=True, upload_to='menu_dishes')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menucategory')),
            ],
        ),
    ]
