# Generated by Django 5.0.3 on 2024-05-01 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_aboutawards'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutawards',
            options={'ordering': ('position',), 'verbose_name_plural': 'Awards'},
        ),
        migrations.AlterModelOptions(
            name='aboutslider',
            options={'ordering': ('position',), 'verbose_name_plural': 'Head Slider'},
        ),
        migrations.AlterModelOptions(
            name='aboutspecial',
            options={'ordering': ('position',), 'verbose_name_plural': 'Special'},
        ),
    ]