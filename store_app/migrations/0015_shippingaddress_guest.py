# Generated by Django 4.2.11 on 2024-04-23 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0014_order_guest'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='guest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store_app.guest'),
        ),
    ]