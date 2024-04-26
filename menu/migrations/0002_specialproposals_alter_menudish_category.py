# Generated by Django 5.0.3 on 2024-04-26 19:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialProposals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='special_proposals/')),
                ('is_visible', models.BooleanField(default=True)),
                ('mark', models.CharField(blank=True, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Special Proposals',
                'ordering': ('-created_at',),
            },
        ),
        migrations.AlterField(
            model_name='menudish',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='menu.menucategory'),
        ),
    ]