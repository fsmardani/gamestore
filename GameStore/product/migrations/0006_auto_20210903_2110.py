# Generated by Django 3.2.6 on 2021-09-03 16:40

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20210903_2102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageproduct',
            name='name',
        ),
        migrations.AlterField(
            model_name='imageproduct',
            name='image',
            field=models.ImageField(upload_to=product.models.model_image_directory_path),
        ),
    ]
