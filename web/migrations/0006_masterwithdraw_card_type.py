# Generated by Django 3.2.25 on 2024-12-03 14:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterwithdraw',
            name='Card_Type',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]
