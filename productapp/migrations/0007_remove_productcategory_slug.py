# Generated by Django 3.2.6 on 2021-08-21 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0006_rename_category_productcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='slug',
        ),
    ]
