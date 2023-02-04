# Generated by Django 4.1.5 on 2023-02-04 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='plan_type',
            field=models.CharField(blank=True, choices=[('BASIC', 'BASIC'), ('POPULAR', 'POPULAR'), ('ENTERPRISE', 'ENTERPRISE')], max_length=30, null=True),
        ),
    ]
