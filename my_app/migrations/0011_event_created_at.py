# Generated by Django 4.2 on 2023-04-22 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0010_makereservation_confirm_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]