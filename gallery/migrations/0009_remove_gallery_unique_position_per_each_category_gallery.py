# Generated by Django 5.0.3 on 2024-05-07 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_alter_gallery_position'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='gallery',
            name='unique_position_per_each_category_gallery',
        ),
    ]