# Generated by Django 2.2.10 on 2020-02-06 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200206_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_category', to='orders.Category'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=models.SET('User Deleted'), related_name='user_order', to=settings.AUTH_USER_MODEL),
        ),
    ]
