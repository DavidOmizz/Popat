# Generated by Django 4.2 on 2023-04-20 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_event_description_event_image_event_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=255, null=True),
        ),
    ]