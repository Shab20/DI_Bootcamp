# Generated by Django 4.1.7 on 2023-03-19 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0005_alter_review_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
