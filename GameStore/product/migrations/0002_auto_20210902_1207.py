# Generated by Django 3.2.6 on 2021-09-02 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category'),
        ),
        migrations.AlterField(
            model_name='imageproduct',
            name='image',
            field=models.ImageField(upload_to='static/img/'),
        ),
    ]
