# Generated by Django 5.0.3 on 2024-04-28 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_bestphrases_phrase'),
    ]

    operations = [
        migrations.AddField(
            model_name='bestphrases',
            name='position',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
