# Generated by Django 4.1.5 on 2023-02-17 14:50

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_alter_client_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='resume',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]