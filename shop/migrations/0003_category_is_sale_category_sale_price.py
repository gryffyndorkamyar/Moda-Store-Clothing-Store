# Generated by Django 5.1 on 2024-08-13 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_category_pprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='category',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
