# Generated by Django 4.1.5 on 2023-02-16 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_linkedin_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkedin',
            name='product',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='linkedin', to='products.product'),
        ),
    ]
