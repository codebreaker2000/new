# Generated by Django 4.1.1 on 2022-09-16 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://www.dirtyapronrecipes.com/wp-content/uploads/2015/10/food-placeholder.png', max_length=500),
        ),
    ]