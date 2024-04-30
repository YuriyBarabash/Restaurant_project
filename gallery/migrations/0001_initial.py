# Generated by Django 5.0.3 on 2024-04-29 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='gallery')),
                ('category', models.CharField(db_index=True, max_length=50, unique=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('position', models.PositiveSmallIntegerField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Gallery',
                'ordering': ('position',),
            },
        ),
    ]