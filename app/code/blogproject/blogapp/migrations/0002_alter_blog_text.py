# Generated by Django 3.2.14 on 2023-05-11 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=models.TextField(max_length=500, verbose_name='本文'),
        ),
    ]
