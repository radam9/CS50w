# Generated by Django 2.2.10 on 2020-02-16 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20200216_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='size',
            field=models.CharField(choices=[('Small', 'Small'), ('Large', 'Large')], default='Large', max_length=5),
        ),
    ]
