# Generated by Django 4.1.5 on 2023-02-17 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_alter_client_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='resume',
            field=models.ImageField(upload_to='resumes'),
        ),
    ]
