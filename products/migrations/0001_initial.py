# Generated by Django 4.1.5 on 2023-01-21 12:38

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('background_type', models.CharField(choices=[('primary', 'primary'), ('secondry', 'secondry'), ('danger', 'danger')], max_length=30)),
                ('plan_type', models.CharField(choices=[('BASIC', 'BASIC'), ('POPULAR', 'POPULAR'), ('ENTERPRISE', 'ENTERPRISE')], max_length=30)),
                ('price', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
                ('description', ckeditor.fields.RichTextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('paid', models.BooleanField(default=False)),
                ('created_on', models.DateField(default=django.utils.timezone.now)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='products.product')),
            ],
        ),
    ]
