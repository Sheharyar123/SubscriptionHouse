# Generated by Django 4.1.5 on 2023-02-16 16:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0018_alter_linkedin_product'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LinkedIn',
            new_name='Client',
        ),
    ]
