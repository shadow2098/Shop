# Generated by Django 4.2.11 on 2024-04-23 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0012_rename_email_customer__email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_guest_username', models.CharField(max_length=200)),
                ('_guest_email', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]