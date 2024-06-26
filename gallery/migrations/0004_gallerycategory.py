# Generated by Django 5.0.3 on 2024-04-29 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_remove_gallery_category_delete_gallerycategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, unique=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('position', models.PositiveSmallIntegerField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Gallery Categories',
                'ordering': ('position',),
            },
        ),
    ]
