# Generated by Django 4.2.11 on 2024-04-23 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0011_rename_passw_customer_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='email',
            new_name='_email',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='gender',
            new_name='_gender',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='password',
            new_name='_password',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='username',
            new_name='_username',
        ),
    ]
