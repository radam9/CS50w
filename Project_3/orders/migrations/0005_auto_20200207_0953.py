# Generated by Django 2.2.10 on 2020-02-07 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20200207_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topping',
            name='category',
            field=models.CharField(choices=[('Pizza', 'Pizza'), ('Subs', 'Subs'), ('Steak+Cheese', 'Steak+Cheese')], max_length=20),
        ),
        migrations.AlterField(
            model_name='topping',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
