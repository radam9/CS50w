# Generated by Django 2.2.10 on 2020-02-16 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20200216_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Order Received', 'Order Received'), ('Preparing', 'Preparing'), ('On Route', 'On Route'), ('Delivered', 'Delivered'), ('None', '')], default='Order Received', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6),
        ),
    ]