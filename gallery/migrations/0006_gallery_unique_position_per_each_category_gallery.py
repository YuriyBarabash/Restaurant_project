# Generated by Django 5.0.3 on 2024-04-29 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_gallery_category'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='gallery',
            constraint=models.UniqueConstraint(fields=('position', 'category'), name='unique_position_per_each_category_gallery'),
        ),
    ]
