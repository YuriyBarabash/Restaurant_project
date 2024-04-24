# Generated by Django 5.0.3 on 2024-04-24 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_menudish'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menucategory',
            old_name='slag',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='menudish',
            old_name='slag',
            new_name='slug',
        ),
        migrations.AddField(
            model_name='menudish',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
    ]