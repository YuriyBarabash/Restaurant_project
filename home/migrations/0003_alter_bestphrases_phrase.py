# Generated by Django 5.0.3 on 2024-04-28 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_bestphrases'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bestphrases',
            name='phrase',
            field=models.TextField(),
        ),
    ]