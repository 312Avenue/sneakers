# Generated by Django 4.0.6 on 2022-07-18 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_order_confirmition_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='confirmition_code',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
