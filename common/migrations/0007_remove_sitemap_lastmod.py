# Generated by Django 3.1.7 on 2022-01-25 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_auto_20220125_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitemap',
            name='lastmod',
        ),
    ]