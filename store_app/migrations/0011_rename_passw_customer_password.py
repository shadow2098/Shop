# Generated by Django 4.2.11 on 2024-04-21 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0010_rename_password_customer_passw'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='passw',
            new_name='password',
        ),
    ]
