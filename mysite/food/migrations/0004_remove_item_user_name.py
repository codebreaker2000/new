# Generated by Django 4.1.1 on 2022-10-29 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_item_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='user_name',
        ),
    ]
