# Generated by Django 4.2.3 on 2023-07-17 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destination',
            old_name='imade',
            new_name='image',
        ),
    ]
