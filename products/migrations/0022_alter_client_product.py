# Generated by Django 4.1.5 on 2023-02-16 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_alter_client_authorized_alter_client_sponsorship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_forms', to='products.product'),
        ),
    ]
