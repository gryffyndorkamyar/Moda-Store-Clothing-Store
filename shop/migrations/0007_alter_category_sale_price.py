# Generated by Django 5.1 on 2024-08-14 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_rename_is_sale_category_osale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='sale_price',
            field=models.CharField(default=False, max_length=100, null=True),
        ),
    ]
