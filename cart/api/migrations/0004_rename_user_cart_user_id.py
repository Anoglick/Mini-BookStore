# Generated by Django 5.1.3 on 2024-12-17 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart_api', '0003_alter_cartitem_product_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='user',
            new_name='user_id',
        ),
    ]
