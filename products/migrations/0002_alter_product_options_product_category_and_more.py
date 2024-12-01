# Generated by Django 5.1.3 on 2024-12-01 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['price'], 'verbose_name': 'App product'},
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('phone', 'Phone')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='contact',
            field=models.TextField(blank=True, null=True, verbose_name='Product Discription'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='photos/24/12/01/camera-icon-png-8.jpg', upload_to='photos/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Product Name'),
        ),
    ]