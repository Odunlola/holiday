# Generated by Django 4.2.3 on 2023-07-19 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spot',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]