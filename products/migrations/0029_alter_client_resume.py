# Generated by Django 4.1.5 on 2023-02-17 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0028_alter_client_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='resume',
            field=models.ImageField(upload_to=''),
        ),
    ]
