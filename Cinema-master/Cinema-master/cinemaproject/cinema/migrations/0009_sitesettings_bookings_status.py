# Generated by Django 4.1.2 on 2022-12-30 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0008_sitesettings_alter_notification_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='bookings_status',
            field=models.BooleanField(default=True),
        ),
    ]
