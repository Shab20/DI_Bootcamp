# Generated by Django 4.1.7 on 2023-03-19 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0002_alter_availability_options_alter_hotel_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='name',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
