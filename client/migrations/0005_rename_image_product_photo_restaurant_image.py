# Generated by Django 4.1.1 on 2022-11-08 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_restaurant_district'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='photo',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]