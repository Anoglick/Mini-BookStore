# Generated by Django 5.1.3 on 2024-12-21 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_api', '0004_rename_user_cart_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='session_key',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
