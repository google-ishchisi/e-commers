# Generated by Django 4.1.2 on 2022-11-04 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photo/products'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photo/products'),
        ),
        migrations.AddField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photo/products'),
        ),
        migrations.AddField(
            model_name='product',
            name='yes_no',
            field=models.IntegerField(blank=True, default=1, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
