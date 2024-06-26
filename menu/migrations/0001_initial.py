# Generated by Django 5.0.3 on 2024-04-26 10:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('position', models.PositiveSmallIntegerField(unique=True)),
                ('icon', models.CharField(blank=True, max_length=50)),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Dish Categories',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='MenuDish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField()),
                ('position', models.PositiveSmallIntegerField()),
                ('photo', models.ImageField(blank=True, upload_to='menu_dishes/')),
                ('is_visible', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menucategory')),
            ],
            options={
                'verbose_name_plural': 'Dishes',
                'ordering': ('position',),
            },
        ),
        migrations.AddConstraint(
            model_name='menudish',
            constraint=models.UniqueConstraint(fields=('position', 'category'), name='unique_position_per_each_category'),
        ),
        migrations.AlterUniqueTogether(
            name='menudish',
            unique_together={('id', 'slug')},
        ),
    ]
