# Generated by Django 5.0.3 on 2024-04-24 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_alter_menudish_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menucategory',
            options={'ordering': ('position',), 'verbose_name_plural': 'Dish Categories'},
        ),
        migrations.AlterModelOptions(
            name='menudish',
            options={'ordering': ('position',), 'verbose_name_plural': 'Dishes'},
        ),
        migrations.AlterUniqueTogether(
            name='menudish',
            unique_together={('id', 'slug')},
        ),
        migrations.AddConstraint(
            model_name='menudish',
            constraint=models.UniqueConstraint(fields=('position', 'category'), name='unique_position_per_each_category'),
        ),
    ]