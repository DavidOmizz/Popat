# Generated by Django 4.2 on 2023-04-21 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0009_event_private_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='makereservation',
            name='Confirm_address',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
