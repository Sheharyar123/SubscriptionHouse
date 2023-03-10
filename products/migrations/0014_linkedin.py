# Generated by Django 4.1.5 on 2023-02-16 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0013_alter_product_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkedIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('job_titles', models.CharField(max_length=255)),
                ('ethnicity', models.CharField(max_length=50)),
                ('race', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=255)),
                ('salary', models.CharField(max_length=255)),
                ('native_language', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=100)),
                ('authorized', models.BooleanField(default=False)),
                ('sponsorship', models.BooleanField(default=False)),
                ('job_type', models.CharField(choices=[('REMOTE', 'REMOTE'), ('HYBRID', 'HYBRID'), ('ON-SITE', 'ON-SITE')], max_length=20)),
                ('disability', models.CharField(blank=True, max_length=255, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linkedin', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
