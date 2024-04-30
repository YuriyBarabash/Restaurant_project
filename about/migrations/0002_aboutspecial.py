# Generated by Django 5.0.3 on 2024-04-30 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSpecial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('phrase', models.TextField()),
                ('photo', models.ImageField(upload_to='about/about_special/')),
                ('is_visible', models.BooleanField(default=True)),
                ('position', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name_plural': 'About Special',
                'ordering': ('position',),
            },
        ),
    ]