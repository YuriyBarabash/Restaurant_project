# Generated by Django 5.0.3 on 2024-04-28 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_bestphrases_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bestphrases',
            options={'ordering': ('position',), 'verbose_name_plural': 'Best Phrases'},
        ),
    ]