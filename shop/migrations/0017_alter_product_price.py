# Generated by Django 4.2.2 on 2024-09-30 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_alter_product_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
    ]
