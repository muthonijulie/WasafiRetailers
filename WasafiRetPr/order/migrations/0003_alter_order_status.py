# Generated by Django 5.1.1 on 2024-10-13 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Canceled', 'Canceled')], default='Pending', max_length=20),
        ),
    ]
