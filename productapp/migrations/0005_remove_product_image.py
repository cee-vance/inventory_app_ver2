# Generated by Django 3.2.6 on 2021-08-13 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0004_auto_20210812_0937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]